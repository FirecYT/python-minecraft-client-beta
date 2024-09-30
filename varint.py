import time

SEGMENT_BITS = 0x7f
CONTINUE_BIT = 0x80

def recv(stream, length):
	result = stream.recv(min(length, 4096))
	last_len = len(result)

	while len(result) < length:
		result += stream.recv(min(length - len(result), 4096))

		if last_len == len(result):
			time.sleep(0.0000001)

		last_len = len(result)

	return result

def convertTo(n):
	result = b''

	while True:
		if n & ~SEGMENT_BITS == 0:
			result += int.to_bytes(n, 1, 'little')
			return result

		result += int.to_bytes((n & SEGMENT_BITS) | CONTINUE_BIT, 1, 'little')

		n >>= 7

def convertFrom(source):
	n = 0
	if callable(getattr(source, 'read', None)):
		read = lambda: int.from_bytes(source.read(1), 'little')
	elif callable(getattr(source, 'recv', None)):
		read = lambda: recv(source, 1)[0]
	else:
		read = lambda: None; return source[n]; n += 1;

	result = 0
	position = 0
	currentByte = 0

	while True:
		currentByte = read()

		result |= (currentByte & SEGMENT_BITS) << position

		if ((currentByte & CONTINUE_BIT) == 0): break

		position += 7

	return result

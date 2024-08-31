import varint, struct
from Packet import reader

DEBUG_MODE = False
JUST = 20

BASE_STRING = lambda name: '┃ ' + ((name + ':').ljust(JUST)) + ' ┃'

def var_debug_stream(format, source, show_remainder = True, skip_header = False, name = '', header = None):
	if not DEBUG_MODE:
		return

	if not skip_header:
		if not header:
			header = (varint.convertFrom(source),  source.read(1)[0])

		length, type = header

		print('\033[44m')
		print("┎────┤ DEBUG ├─────────┰────┤ " + name + " ├─────┄┄┄┄")

		print('┃', 'Lenght:'.ljust(JUST), '┃', str(length).ljust(8), "{:019_b}".format(length).replace('_', ' '))
		print('┃  ', '┃'.rjust(JUST))

		print('┃', 'Type:'.ljust(JUST), '┃', "\033[45m{:#04x}\033[44m".format(type))
		print('┃  ', '┃'.rjust(JUST))

	for data in format:
		name = data[0]
		type = data[1]

		if len(data) >= 3:
			value = data[2]

		if type in (
			'bool',
			'byte',
			'varint',
			'short',
			'float',
			'double',
			'int',
			'long',
			'uuid',
			'angle',
		):
			print(
				BASE_STRING(name),
				reader(source, type)
			)
		elif type == 'str':
			LEN = varint.convertFrom(source)

			print(
				BASE_STRING(name + ' LEN'),
				LEN
			)
			print(
				BASE_STRING(name + ' STR'),
				source.read(LEN)
			)
		elif type == 'custom':
			print(
				BASE_STRING(name),
				value
			)
		else:
			print(type)
		print('┃  ', '┃'.rjust(JUST))

	if show_remainder:
		print('┃', 'Remainder:'.ljust(JUST), '┃', source.read())
		print("┖──────────────────────┸────────────┄┄┄┄\033[m")
		print()


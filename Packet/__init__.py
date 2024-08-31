from typing import SupportsBytes
from varint import convertTo, convertFrom
from socket import socket
from struct import pack, unpack
from uuid import UUID

def reader(source, type):
	if type == 'varint':
		return convertFrom(source)
	elif type == 'str':
		length = convertFrom(source)
		return source.read(length).decode()
	elif type == 'bool':
		return unpack('?', source.read(1))[0]
	elif type == 'byte':
		return unpack('b', source.read(1))[0]
	elif type == 'angle':
		return unpack('b', source.read(1))[0]
	elif type == 'short':
		return unpack('>h', source.read(2))[0]
	elif type == 'float':
		return unpack('>f', source.read(4))[0]
	elif type == 'double':
		return unpack('>d', source.read(8))[0]
	elif type == 'int':
		return unpack('>i', source.read(4))[0]
	elif type == 'long':
		buffer = source.read(8)
		return unpack('q', buffer)[0]
	elif type == 'uuid':
		return str(UUID(bytes=source.read(16)))

class BasePacket(SupportsBytes, object):
	PACKET_ID = None
	PACKET_DIRECTION = None

	def __init__(self):
		pass

	def __bytes__(self):
		result = convertTo(self.PACKET_ID) + self.bytes()
		result = convertTo(len(result)) + result

		return result

	def bytes(self):
		raise NotImplementedError()

	def write(self, stream: socket):
		stream.sendall(bytes(self))

	@classmethod
	def read(cls, stream: socket):
		raise NotImplementedError()

class HandshakePacket(BasePacket):
	PACKET_ID = 0x00
	PACKET_DIRECTION = "SERVERBOUND"

	def __init__(self, protocol, hostname, port, next_state):
		BasePacket.__init__(self)
		self._protocol = int(protocol)
		self._hostname = str(hostname)
		self._port = int(port)
		self._next_state = int(next_state)

	def bytes(self):
		result = b''

		result += convertTo(self._protocol)
		result += convertTo(len(self._hostname)) + self._hostname.encode()
		result += pack('h', self._port)
		result += convertTo(self._next_state)

		return result

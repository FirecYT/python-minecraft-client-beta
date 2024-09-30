from Packet import BasePacket, reader
from varint import convertTo
from socket import socket
from struct import pack

class TeleportConfirm(BasePacket):
	PACKET_ID = 0x00

	def __init__(self, teleport_id):
		BasePacket.__init__(self)
		self._teleport_id = teleport_id

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			teleport_id = reader(stream, 'varint'),
		)

	def bytes(self):
		result = convertTo(self._teleport_id)

		return result

class ChatMessage(BasePacket):
	PACKET_ID = 0x03

	def __init__(self, string):
		BasePacket.__init__(self)
		self._string = string

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			string = reader(stream, 'str'),
		)

	def bytes(self):
		result = b''

		result += convertTo(len(self._string)) + self._string.encode()

		return result

class KeepAlive(BasePacket):
	PACKET_ID = 0x0F

	def __init__(self, keep_id):
		BasePacket.__init__(self)
		self._keep_id = keep_id

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			keep_id = reader(stream, 'long')
		)

	def bytes(self):
		result = pack('q', self._keep_id)

		return result

class PlayerPosition(BasePacket):
	PACKET_ID = 0x11

	def __init__(self, x, y, z, on_ground):
		BasePacket.__init__(self)
		self._x = x
		self._y = y
		self._z = z
		self._on_ground = on_ground

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			x			= reader(stream, 'double'),
			y			= reader(stream, 'double'),
			z			= reader(stream, 'double'),
			on_ground	= reader(stream, 'bool')
		)

	def bytes(self):
		result = b''

		result += pack('d', self._x)
		result += pack('d', self._y)
		result += pack('d', self._z)
		result += pack('?', self._on_ground)

		return result

class PlayerPosition(BasePacket):
	PACKET_ID = 0x11

	def __init__(self, x, y, z, yaw, pitch, on_ground):
		BasePacket.__init__(self)
		self._x = x
		self._y = y
		self._z = z
		self._yaw = yaw
		self._pitch = pitch
		self._on_ground = on_ground

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			x			= reader(stream, 'double'),
			y			= reader(stream, 'double'),
			z			= reader(stream, 'double'),
			on_ground	= reader(stream, 'bool')
		)

	def bytes(self):
		result = b''

		result += pack('>d', self._x)
		result += pack('>d', self._y)
		result += pack('>d', self._z)
		result += pack('>?', self._on_ground)

		return result

class PlayerPositionAndLook(BasePacket):
	PACKET_ID = 0x12

	def __init__(self, x, y, z, yaw, pitch, on_ground):
		BasePacket.__init__(self)
		self._x = x
		self._y = y
		self._z = z
		self._yaw = yaw
		self._pitch = pitch
		self._on_ground = on_ground

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			x			= reader(stream, 'double'),
			y			= reader(stream, 'double'),
			z			= reader(stream, 'double'),
			yaw			= reader(stream, 'float'),
			pitch		= reader(stream, 'float'),
			on_ground	= reader(stream, 'bool')
		)

	def bytes(self):
		result = b''

		result += pack('>d', self._x)
		result += pack('>d', self._y)
		result += pack('>d', self._z)
		result += pack('>f', self._yaw)
		result += pack('>f', self._pitch)
		result += pack('>?', self._on_ground)

		return result

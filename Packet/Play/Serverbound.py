from Packet import BasePacket, reader
from socket import socket

class SpawnEntity(BasePacket):
	PACKET_ID = 0x00

	def __init__(self, entity_id, entity_uuid, type, x, y, z, yaw, pitch, data, velocity_x, velocity_y, velocity_z):
		BasePacket.__init__(self)
		self._entity_id = int(entity_id)
		self._entity_uuid = str(entity_uuid)
		self._type = int(type)
		self._x = float(x)
		self._y = float(y)
		self._z = float(z)
		self._yaw = int(yaw)
		self._pitch = int(pitch)
		self._data = int(data)
		self._velocity_x = float(velocity_x)
		self._velocity_y = float(velocity_y)
		self._velocity_z = float(velocity_z)

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			entity_id		= reader(stream, 'varint'),
			entity_uuid		= reader(stream, 'uuid'),
			type			= reader(stream, 'varint'),
			x				= reader(stream, 'double'),
			y				= reader(stream, 'double'),
			z				= reader(stream, 'double'),
			yaw				= reader(stream, 'angle'),
			pitch			= reader(stream, 'angle'),
			data			= reader(stream, 'int'),
			velocity_x		= reader(stream, 'short'),
			velocity_y		= reader(stream, 'short'),
			velocity_z		= reader(stream, 'short')
		)

class SpawnLivingEntity(BasePacket):
	PACKET_ID = 0x02

	def __init__(self, entity_id, entity_uuid, type, x, y, z, yaw, pitch, head_pitch, velocity_x, velocity_y, velocity_z):
		BasePacket.__init__(self)
		self._entity_id = int(entity_id)
		self._entity_uuid = str(entity_uuid)
		self._type = int(type)
		self._x = float(x)
		self._y = float(y)
		self._z = float(z)
		self._yaw = int(yaw)
		self._pitch = int(pitch)
		self._head_pitch = int(head_pitch)
		self._velocity_x = float(velocity_x)
		self._velocity_y = float(velocity_y)
		self._velocity_z = float(velocity_z)

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			entity_id		= reader(stream, 'varint'),
			entity_uuid		= reader(stream, 'uuid'),
			type			= reader(stream, 'varint'),
			x				= reader(stream, 'double'),
			y				= reader(stream, 'double'),
			z				= reader(stream, 'double'),
			yaw				= reader(stream, 'angle'),
			pitch			= reader(stream, 'angle'),
			head_pitch		= reader(stream, 'angle'),
			velocity_x		= reader(stream, 'short'),
			velocity_y		= reader(stream, 'short'),
			velocity_z		= reader(stream, 'short')
		)

class SpawnPlayer(BasePacket):
	PACKET_ID = 0x04

	def __init__(self, entity_id, player, x, y, z, yaw, pitch):
		BasePacket.__init__(self)
		self._entity_id = entity_id
		self._player = player
		self._x = x
		self._y = y
		self._z = z
		self._yaw = yaw
		self._pitch = pitch

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			entity_id	 = reader(stream, 'varint'),
			player		 = reader(stream, 'uuid'),
			x			 = reader(stream, 'double'),
			y			 = reader(stream, 'double'),
			z			 = reader(stream, 'double'),
			yaw			 = reader(stream, 'angle'),
			pitch		 = reader(stream, 'angle')
		)

class ChatMessage(BasePacket):
	PACKET_ID = 0x0F

	def __init__(self, data, position, sender):
		BasePacket.__init__(self)
		self._data = data
		self._position = position
		self._sender = sender

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			data		 = reader(stream, 'str'),
			position	 = reader(stream, 'byte'),
			sender		 = reader(stream, 'uuid'),
		)

class Disconnect(BasePacket):
	PACKET_ID = 0x1A

	def __init__(self, reason):
		BasePacket.__init__(self)
		self._reason = reason

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			reason		 = reader(stream, 'str'),
		)

class KeepAlive(BasePacket):
	PACKET_ID = 0x21

	def __init__(self, keep_id):
		BasePacket.__init__(self)
		self._keep_id = keep_id

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			keep_id = reader(stream, 'long')
		)

class PlayerPositionAndLook(BasePacket):
	PACKET_ID = 0x38

	def __init__(self, x, y, z, yaw, pitch, flags, teleport_id, dismount_vehicle):
		BasePacket.__init__(self)
		self._x = x
		self._y = y
		self._z = z
		self._yaw = yaw
		self._pitch = pitch
		self._flags = flags
		self._teleport_id = teleport_id
		self._dismount_vehicle = dismount_vehicle

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			x					= reader(stream, 'double'),
			y					= reader(stream, 'double'),
			z					= reader(stream, 'double'),
			yaw					= reader(stream, 'float'),
			pitch				= reader(stream, 'float'),
			flags				= reader(stream, 'byte'),
			teleport_id			= reader(stream, 'varint'),
			dismount_vehicle	= reader(stream, 'bool')
		)

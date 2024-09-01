from Packet import BasePacket, reader
from varint import convertTo
from socket import socket
from struct import pack

class ChatMessage(BasePacket):
	PACKET_ID = 0x03

	def __init__(self, string):
		BasePacket.__init__(self)
		self._string = string

	@classmethod
	def read(cls: BasePacket, stream: socket):
		return cls(
			string		 = reader(stream, 'str'),
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

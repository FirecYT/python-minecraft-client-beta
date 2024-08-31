from Packet import BasePacket, reader
from varint import convertTo
from socket import socket

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

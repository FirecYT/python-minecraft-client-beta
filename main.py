import Packet
import Packet.Play.Serverbound as Serverbound
import Packet.Play.Clientbound as Clientbound

import nbt.nbt
import varint, io, debug, time, nbt, json

from packet_names import PACKET_NAMES
import socket as S

import tkinter, mobs, map, chat, PlayerPositionAndLook, enemis3D
from tkinter import ttk

def packetGenerator(packet_id, format):
	result = b''

	result += varint.convertTo(packet_id)

	for (type, value) in format:
		if type == 'varint':
			result += varint.convertTo(value)
		elif type == 'string':
			result += varint.convertTo(len(value)) + value.encode()
		elif type == 'short':
			result += int.to_bytes(value, 2, 'little')
		elif type == 'int':
			result += int.to_bytes(value, 4, 'little')
		elif type == 'long':
			result += int.to_bytes(value, 8, 'little')
		else:
			result += value

	result = varint.convertTo(len(result)) + result

	return result

# TODO: Допилить
HOST = '192.168.1.100'
PORT = 25565

JUST = 12

# Init connection

socket = S.socket(S.AF_INET, S.SOCK_STREAM)
socket.connect((HOST, PORT))
socket.settimeout(1)

print('Connected to: ', HOST)



state = 2

handshake = Packet.HandshakePacket(
	757,
	HOST,
	25565,
	state
)

stream = io.BytesIO(bytes(handshake))
debug.var_debug_stream([
	('Version', 'varint'),
	('Addr', 'str'),
	('Port', 'short'),
	('State', 'varint'),
], stream)

print('Send data...')
socket.sendall(bytes(handshake))

if state == 1:
	socket.sendall(b'\x01\x00')
	length = varint.convertFrom(socket)
	response = socket.recv(length)
	stream = io.BytesIO(varint.convertTo(length) + response)

	debug.var_debug_stream([
		('JSON', 'str'),
	], stream)

	exit()



packet = packetGenerator(0x00, [
	('string', 'FirecFT'),        # Nickname
	# ('long', 14341347382891133688), # UUID
	# ('long', 10620945300516742842),
])

stream = io.BytesIO(packet)
debug.var_debug_stream([
	('Nickname', 'str'),
	# ('UUID', 'long'),
	# ('UUID', 'long'),
], stream)

print('Send data...')
socket.sendall(packet)



print()
print('Read data...')

length = varint.convertFrom(socket)
response = socket.recv(length)
stream = io.BytesIO(varint.convertTo(length) + response)

debug.var_debug_stream([
	('UUID', 'uuid'),
	('Nickname', 'str'),
], stream)



# Блядский род, это нужно для более новой версии Minecraft
# packet = packetGenerator(0x03, [])

# stream = io.BytesIO(packet)
# debug.var_debug_stream([], stream)

# print('Send data...')
# socket.sendall(packet)



print('''\033[41m\n┎────┤ WOW! ├────┒\n┃    Logined!    ┃\n┖────────────────┚\033[0m''')



packets = {}

root = tkinter.Tk()

# root.geometry('500x500')

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

mobs_window = mobs.Window(notebook)
map_window = map.Window(notebook)
chat_window = chat.Window(notebook)
playerPositionAndLook = PlayerPositionAndLook.Window(notebook)
mobs3d_window = enemis3D.Window(notebook, width=320, height=200)

mobs_window.pack(fill='both', expand=True)
map_window.pack(fill='both', expand=True)
chat_window.pack(fill='both', expand=True)
playerPositionAndLook.pack(fill='both', expand=True)
mobs3d_window.pack(fill='both', expand=True)
mobs3d_window.animate = 1

notebook.add(mobs_window, text="Mobs")
notebook.add(map_window, text="Map")
notebook.add(chat_window, text="Chat")
notebook.add(playerPositionAndLook, text="Player")
notebook.add(mobs3d_window, text="Mobs3D")

def sendMessage(event):
	text = chat_window.input.get()

	packet = Clientbound.ChatMessage(text)

	packet.write(socket)

chat_window.button.bind('<Button-1>', sendMessage)



time.sleep(1)

print()
print('Read data...')

while True:
# for x in range(5):
	root.update()

	length = varint.convertFrom(socket)

	response = b''.join([socket.recv(1024) for i in range(length // 1024)])

	if length - length // 1024 > 0:
		response += socket.recv(length - length // 1024)

	stream = io.BytesIO(varint.convertTo(length) + response)

	try:
		packet_id = response[0]
	except:
		print(length, response)

	if packet_id == 0x26:
		debug.var_debug_stream([
			('Entity ID', 'int'),
			('Is Hard', 'bool'),
			('Gamemode', 'byte'),
			('Last gamemode', 'byte'),
		], stream, show_remainder = False, name=PACKET_NAMES[0x26])

		if debug.DEBUG_MODE:
			worlds_count = varint.convertFrom(stream)

			data = [
				('Dimension Name', 'str'),
				('Seed', 'long'),
				('Max Players', 'varint'),
				('View Distance', 'varint'),
				('Simulation', 'varint'),
				('Debug Info', 'bool'),
				('Respawn screen', 'bool'),
				('Is Debug', 'bool'),
				('Is Flat', 'bool'),
			]

			data.insert(-1, ('Worlds Count', 'custom', worlds_count))
			[data.insert(-1, ('World', 'custom', stream.read(varint.convertFrom(stream)))) for val in range(worlds_count)]

			first = nbt.nbt.NBTFile(False, stream)
			second = nbt.nbt.NBTFile(False, stream)
			# print(json.dumps(
			# 	second,
			# 	default=lambda o: o.__dict__,
			# 	sort_keys=True,
			# 	indent=4
			# ))

			debug.var_debug_stream(data, stream, skip_header=True, name=PACKET_NAMES[0x26])
	elif packet_id == 0x18:
		debug.var_debug_stream([
			('Channel', 'str'),
		], stream, show_remainder = False, name=PACKET_NAMES[0x18])
	elif packet_id == 0x0e:
		debug.var_debug_stream([
			('Difficulty', 'byte'),
			('Is Look', 'bool'),
		], stream, name=PACKET_NAMES[0x0e])
	elif packet_id == 0x32:
		debug.var_debug_stream([
			('Flags', 'byte'),
			('Flying Speed', 'float'),
			('FOV Modifier', 'float'),
		], stream, name=PACKET_NAMES[0x32])
	elif packet_id == 0x48:
		debug.var_debug_stream([
			('Slot', 'byte'),
		], stream, name=PACKET_NAMES[0x48])
	elif packet_id == Serverbound.SpawnLivingEntity.PACKET_ID:
		header = (varint.convertFrom(stream),  stream.read(1)[0])
		packet = Serverbound.SpawnLivingEntity.read(stream)

		mobs_window.listbox.insert(0, mobs.MOBS[packet._type]['name'] + " #" + str(packet._entity_id))
		mobs_window.mobs.insert(0, packet)

		mobs3d_window.cubes.append(
			(
				(packet._x - int(playerPositionAndLook.label_x['text'])) / 10,
				(packet._y - int(playerPositionAndLook.label_y['text'])) / 10,
				(packet._z - int(playerPositionAndLook.label_z['text'])) / 10,
				0.5, (1, 0, 1)
			)
		)

		map_window.canvas.create_oval(
			250 + (packet._x - int(playerPositionAndLook.label_x['text'])),
			250 + (packet._z - int(playerPositionAndLook.label_z['text'])),
			250 + (packet._x - int(playerPositionAndLook.label_x['text'])) + 1,
			250 + (packet._z - int(playerPositionAndLook.label_z['text'])) + 1,
			fill='black'
		)
	elif packet_id == Serverbound.SpawnEntity.PACKET_ID:
		header = (varint.convertFrom(stream),  stream.read(1)[0])
		print(length, header, len(response))
		packet = Serverbound.SpawnEntity.read(stream)

		mobs_window.listbox.insert(0, mobs.MOBS[packet._type]['name'] + " #" + str(packet._entity_id))
		mobs_window.mobs.insert(0, packet)

		mobs3d_window.cubes.append(
			(
				(packet._x - int(playerPositionAndLook.label_x['text'])) / 10,
				(packet._y - int(playerPositionAndLook.label_y['text'])) / 10,
				(packet._z - int(playerPositionAndLook.label_z['text'])) / 10,
				0.25, (1, 1, 0)
			)
		)

		map_window.canvas.create_oval(
			250 + (packet._x - int(playerPositionAndLook.label_x['text'])),
			250 + (packet._z - int(playerPositionAndLook.label_z['text'])),
			250 + (packet._x - int(playerPositionAndLook.label_x['text'])) + 1,
			250 + (packet._z - int(playerPositionAndLook.label_z['text'])) + 1,
			fill='gold'
		)
	elif packet_id == Serverbound.SpawnPlayer.PACKET_ID:
		header = (varint.convertFrom(stream),  stream.read(1)[0])
		packet = Serverbound.SpawnPlayer.read(stream)

		mobs_window.listbox.insert(0, "Player #" + str(packet._entity_id))
		mobs_window.mobs.insert(0, packet)
	elif packet_id == Serverbound.ChatMessage.PACKET_ID:
		header = (varint.convertFrom(stream),  stream.read(1)[0])
		packet = Serverbound.ChatMessage.read(stream)

		data = json.loads(packet._data)

		chat_window.text.insert('end', data["text"] + "\n")

		for extra in data["extra"]:
			tags = ()
			if "bold" in extra and extra["bold"]:
				tags += ("bold", )
			if "underlined" in extra and extra["underlined"]:
				tags += ("underlined", )
			if "strikethrough" in extra and extra["strikethrough"]:
				tags += ("strikethrough", )
			if "obfuscated" in extra and extra["obfuscated"]:
				tags += ("obfuscated", )
			if "color" in extra and extra["color"]:
				tags += ("color_" + extra["color"], )

			if 'text' in extra:
				print(extra["text"], tags)
				chat_window.text.insert('end', extra['text'], tags)
			else:
				chat_window.text.insert('end', packet._data, tags)
	elif packet_id == Serverbound.Disconnect.PACKET_ID:
		header = (varint.convertFrom(stream),  stream.read(1)[0])
		packet = Serverbound.Disconnect.read(stream)

		debug.var_debug_stream([
			('Reason', 'custom', packet._reason),
		], stream, name=PACKET_NAMES[Serverbound.Disconnect.PACKET_ID])
	elif packet_id == Serverbound.PlayerPositionAndLook.PACKET_ID:
		header = (varint.convertFrom(stream),  stream.read(1)[0])
		packet = Serverbound.PlayerPositionAndLook.read(stream)

		debug.var_debug_stream([
			('x', 'custom', packet._x),
			('y', 'custom', packet._y),
			('z', 'custom', packet._z),
			('yaw', 'custom', packet._yaw),
			('pitch', 'custom', packet._pitch),
			('flags', 'custom', packet._flags),
			('teleport_id', 'custom', packet._teleport_id),
			('dismount_vehicle', 'custom', packet._dismount_vehicle),
		], stream, header=header, name=PACKET_NAMES[Serverbound.PlayerPositionAndLook.PACKET_ID])

		playerPositionAndLook.label_x['text'] = packet._x
		playerPositionAndLook.label_y['text'] = packet._y
		playerPositionAndLook.label_z['text'] = packet._z
		playerPositionAndLook.label_yaw['text'] = "yaw" + str(packet._yaw)
		playerPositionAndLook.label_pitch['text'] = "pitch" + str(packet._pitch)
		playerPositionAndLook.label_flags['text'] = "flags" + str(packet._flags)
		playerPositionAndLook.label_teleport_id['text'] = "teleport_id" + str(packet._teleport_id)
		playerPositionAndLook.label_dismount_vehicle['text'] = "dismount_vehicle" + str(packet._dismount_vehicle)

		map_window.canvas.create_oval(
			250,
			250,
			250 + 5,
			250 + 5,
			fill='red'
		)

		map_window.canvasLeft.create_oval(
			250,
			250,
			250 + 5,
			250 + 5,
			fill='black'
		)

		map_window.canvasFront.create_oval(
			250,
			250,
			250 + 5,
			250 + 5,
			fill='black'
		)
	elif packet_id == 0x3e:
		debug.var_debug_stream([
			('Entity ID', 'varint'),
			('Head', 'byte'),
		], stream, name=PACKET_NAMES[0x3e])
	elif packet_id == 0x4d:
		debug.var_debug_stream([
			('Entity ID', 'varint'),
		], stream, name=PACKET_NAMES[0x4d])
	else:
		pack_name = "{:#04x}".format(packet_id)

		if not pack_name in packets:
			packets[pack_name] = 0
		packets[pack_name] += 1

		if debug.DEBUG_MODE:
			print(pack_name)

	time.sleep(0.01)

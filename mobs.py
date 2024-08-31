import tkinter
from tkinter import ttk
from Packet.Play.Serverbound import SpawnLivingEntity

class Window(tkinter.Frame, tkinter.Tk):
	def __init__(self, master=None, cnf={}, **args):
		super().__init__(master, cnf, **args)

		try:
			self.title('Mobs')
			self.geometry('400x250')
		except Exception:
			pass



		self.mobs = []
		self.listbox = tkinter.Listbox(self, listvariable=tkinter.Variable(value=[]))
		scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.listbox.yview)

		frame_data = ttk.Frame(self, borderwidth=1, relief='solid')
		frame_position = ttk.Frame(self, borderwidth=1, relief='solid')
		frame_angle = ttk.Frame(self, borderwidth=1, relief='solid')
		frame_velocity = ttk.Frame(self, borderwidth=1, relief='solid')

		self.label_entity_id = ttk.Label(frame_data, text="entity_id", justify = 'left')
		self.label_entity_uuid = ttk.Label(frame_data, text="entity_uuid", justify = 'left')
		self.label_type = ttk.Label(frame_data, text="type", justify = 'left')

		self.label_x = ttk.Label(frame_position, text="x", justify = 'left')
		self.label_y = ttk.Label(frame_position, text="y", justify = 'left')
		self.label_z = ttk.Label(frame_position, text="z", justify = 'left')

		self.label_yaw = ttk.Label(frame_angle, text="yaw", justify = 'left')
		self.label_pitch = ttk.Label(frame_angle, text="pitch", justify = 'left')
		self.label_head_pitch = ttk.Label(frame_angle, text="head_pitch", justify = 'left')

		self.label_velocity_x = ttk.Label(frame_velocity, text="velocity_x", justify = 'left')
		self.label_velocity_y = ttk.Label(frame_velocity, text="velocity_y", justify = 'left')
		self.label_velocity_z = ttk.Label(frame_velocity, text="velocity_z", justify = 'left')



		self.columnconfigure(index = 0, weight = 0)
		self.columnconfigure(index = 1, weight = 0)
		self.columnconfigure(index = 2, weight = 1)

		self.rowconfigure(index = 0, weight = 1)
		self.rowconfigure(index = 1, weight = 1)
		self.rowconfigure(index = 2, weight = 1)
		self.rowconfigure(index = 3, weight = 1)

		self.label_entity_id.pack(fill = 'both')
		self.label_entity_uuid.pack(fill = 'both')
		self.label_type.pack(fill = 'both')
		self.label_x.pack(fill = 'both')
		self.label_y.pack(fill = 'both')
		self.label_z.pack(fill = 'both')
		self.label_yaw.pack(fill = 'both')
		self.label_pitch.pack(fill = 'both')
		self.label_head_pitch.pack(fill = 'both')
		self.label_velocity_x.pack(fill = 'both')
		self.label_velocity_y.pack(fill = 'both')
		self.label_velocity_z.pack(fill = 'both')

		self.listbox.grid(row = 0, column = 0, rowspan = 4, sticky = 'nsew')
		scrollbar.grid(row = 0, column = 1, rowspan = 4, sticky = 'nsew')

		frame_data.grid(row = 0, column = 2, sticky = 'nsew')
		frame_position.grid(row = 1, column = 2, sticky = 'nsew')
		frame_angle.grid(row = 2, column = 2, sticky = 'nsew')
		frame_velocity.grid(row = 3, column = 2, sticky = 'nsew')



		self.listbox["yscrollcommand"] = scrollbar.set
		self.listbox.bind("<<ListboxSelect>>", self.selected)

	def selected(self, event):
		# получаем индексы выделенных элементов
		selected_index = self.listbox.curselection()[0]
		_packet = self.listbox.get(selected_index)
		packet: SpawnLivingEntity = self.mobs[selected_index]

		self.label_entity_id['text'] = "entity_id: " + str(packet._entity_id) + " " + MOBS[packet._type]['name']
		self.label_entity_uuid['text'] = "entity_uuid: " + str(packet._entity_uuid)
		self.label_type['text'] = "type: " + str(packet._type)
		self.label_x['text'] = "x: " + str(packet._x)
		self.label_y['text'] = "y: " + str(packet._y)
		self.label_z['text'] = "z: " + str(packet._z)
		self.label_yaw['text'] = "yaw: " + str(packet._yaw)
		self.label_pitch['text'] = "pitch: " + str(packet._pitch)
		self.label_head_pitch['text'] = "head_pitch: " + str(packet._head_pitch)
		self.label_velocity_x['text'] = "velocity_x: " + str(packet._velocity_x)
		self.label_velocity_y['text'] = "velocity_y: " + str(packet._velocity_y)
		self.label_velocity_z['text'] = "velocity_z: " + str(packet._velocity_z)

MOBS = [
	{
		"type": 0,
		"name": "Area Effect Cloud",
		"box_xz": "2.0 * Radius",
		"box_y": "0.5",
		"ID": "minecraft:area_effect_cloud"
	},
	{
		"type": 1,
		"name": "Armor Stand",
		"box_xz": "normal: 0.5 marker: 0.0 small: 0.25",
		"box_y": "normal: 1.975 marker: 0.0 small: 0.9875",
		"ID": "minecraft:armor_stand"
	},
	{
		"type": 2,
		"name": "Arrow",
		"box_xz": "0.5",
		"box_y": "0.5",
		"ID": "minecraft:arrow"
	},
	{
		"type": 3,
		"name": "Axolotl",
		"box_xz": "1.3",
		"box_y": "0.6",
		"ID": "minecraft:axolotl"
	},
	{
		"type": 4,
		"name": "Bat",
		"box_xz": "0.5",
		"box_y": "0.9",
		"ID": "minecraft:bat"
	},
	{
		"type": 5,
		"name": "Bee",
		"box_xz": "0.7",
		"box_y": "0.6",
		"ID": "minecraft:bee"
	},
	{
		"type": 6,
		"name": "Blaze",
		"box_xz": "0.6",
		"box_y": "1.8",
		"ID": "minecraft:blaze"
	},
	{
		"type": 7,
		"name": "Boat",
		"box_xz": "1.375",
		"box_y": "0.5625",
		"ID": "minecraft:boat"
	},
	{
		"type": 8,
		"name": "Cat",
		"box_xz": "0.6",
		"box_y": "0.7",
		"ID": "minecraft:cat"
	},
	{
		"type": 9,
		"name": "Cave Spider",
		"box_xz": "0.7",
		"box_y": "0.5",
		"ID": "minecraft:cave_spider"
	},
	{
		"type": 10,
		"name": "Chicken",
		"box_xz": "0.4",
		"box_y": "0.7",
		"ID": "minecraft:chicken"
	},
	{
		"type": 11,
		"name": "Cod",
		"box_xz": "0.5",
		"box_y": "0.3",
		"ID": "minecraft:cod"
	},
	{
		"type": 12,
		"name": "Cow",
		"box_xz": "0.9",
		"box_y": "1.4",
		"ID": "minecraft:cow"
	},
	{
		"type": 13,
		"name": "Creeper",
		"box_xz": "0.6",
		"box_y": "1.7",
		"ID": "minecraft:creeper"
	},
	{
		"type": 14,
		"name": "Dolphin",
		"box_xz": "0.9",
		"box_y": "0.6",
		"ID": "minecraft:dolphin"
	},
	{
		"type": 15,
		"name": "Donkey",
		"box_xz": "1.5",
		"box_y": "1.39648",
		"ID": "minecraft:donkey"
	},
	{
		"type": 16,
		"name": "Dragon Fireball",
		"box_xz": "1.0",
		"box_y": "1.0",
		"ID": "minecraft:dragon_fireball"
	},
	{
		"type": 17,
		"name": "Drowned",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:drowned"
	},
	{
		"type": 18,
		"name": "Elder Guardian",
		"box_xz": "1.9975 (2.35 * guardian)",
		"box_y": "1.9975 (2.35 * guardian)",
		"ID": "minecraft:elder_guardian"
	},
	{
		"type": 19,
		"name": "End Crystal",
		"box_xz": "2.0",
		"box_y": "2.0",
		"ID": "minecraft:end_crystal"
	},
	{
		"type": 20,
		"name": "Ender Dragon",
		"box_xz": "16.0",
		"box_y": "8.0",
		"ID": "minecraft:ender_dragon"
	},
	{
		"type": 21,
		"name": "Enderman",
		"box_xz": "0.6",
		"box_y": "2.9",
		"ID": "minecraft:enderman"
	},
	{
		"type": 22,
		"name": "Endermite",
		"box_xz": "0.4",
		"box_y": "0.3",
		"ID": "minecraft:endermite"
	},
	{
		"type": 23,
		"name": "Evoker",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:evoker"
	},
	{
		"type": 24,
		"name": "Evoker Fangs",
		"box_xz": "0.5",
		"box_y": "0.8",
		"ID": "minecraft:evoker_fangs"
	},
	{
		"type": 25,
		"name": "Experience Orb",
		"box_xz": "0.5",
		"box_y": "0.5",
		"ID": "minecraft:experience_orb"
	},
	{
		"type": 26,
		"name": "Eye of Ender",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:eye_of_ender"
	},
	{
		"type": 27,
		"name": "Falling Block",
		"box_xz": "0.98",
		"box_y": "0.98",
		"ID": "minecraft:falling_block"
	},
	{
		"type": 28,
		"name": "Firework Rocket Entity",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:firework_rocket"
	},
	{
		"type": 29,
		"name": "Fox",
		"box_xz": "0.6",
		"box_y": "0.7",
		"ID": "minecraft:fox"
	},
	{
		"type": 30,
		"name": "Ghast",
		"box_xz": "4.0",
		"box_y": "4.0",
		"ID": "minecraft:ghast"
	},
	{
		"type": 31,
		"name": "Giant",
		"box_xz": "3.6",
		"box_y": "12.0",
		"ID": "minecraft:giant"
	},
	{
		"type": 32,
		"name": "Glow Item Frame",
		"box_xz": "0.75 or 0.0625 (depth)",
		"box_y": "0.75",
		"ID": "minecraft:glow_item_frame"
	},
	{
		"type": 33,
		"name": "Glow Squid",
		"box_xz": "0.8",
		"box_y": "0.8",
		"ID": "minecraft:glow_squid"
	},
	{
		"type": 34,
		"name": "Goat",
		"box_xz": "1.3 (adult), 0.65 (baby)",
		"box_y": "0.9 (adult), 0.45 (baby)",
		"ID": "minecraft:goat"
	},
	{
		"type": 35,
		"name": "Guardian",
		"box_xz": "0.85",
		"box_y": "0.85",
		"ID": "minecraft:guardian"
	},
	{
		"type": 36,
		"name": "Hoglin",
		"box_xz": "1.39648",
		"box_y": "1.4",
		"ID": "minecraft:hoglin"
	},
	{
		"type": 37,
		"name": "Horse",
		"box_xz": "1.39648",
		"box_y": "1.6",
		"ID": "minecraft:horse"
	},
	{
		"type": 38,
		"name": "Husk",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:husk"
	},
	{
		"type": 39,
		"name": "Illusioner",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:illusioner"
	},
	{
		"type": 40,
		"name": "Iron Golem",
		"box_xz": "1.4",
		"box_y": "2.7",
		"ID": "minecraft:iron_golem"
	},
	{
		"type": 41,
		"name": "Item",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:item"
	},
	{
		"type": 42,
		"name": "Item Frame",
		"box_xz": "0.75 or 0.0625 (depth)",
		"box_y": "0.75",
		"ID": "minecraft:item_frame"
	},
	{
		"type": 43,
		"name": "Fireball",
		"box_xz": "1.0",
		"box_y": "1.0",
		"ID": "minecraft:fireball"
	},
	{
		"type": 44,
		"name": "Leash Knot",
		"box_xz": "0.375",
		"box_y": "0.5",
		"ID": "minecraft:leash_knot"
	},
	{
		"type": 45,
		"name": "Lightning Bolt",
		"box_xz": "0.0",
		"box_y": "0.0",
		"ID": "minecraft:lightning_bolt"
	},
	{
		"type": 46,
		"name": "Llama",
		"box_xz": "0.9",
		"box_y": "1.87",
		"ID": "minecraft:llama"
	},
	{
		"type": 47,
		"name": "Llama Spit",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:llama_spit"
	},
	{
		"type": 48,
		"name": "Magma Cube",
		"box_xz": "0.51000005 * size",
		"box_y": "0.51000005 * size",
		"ID": "minecraft:magma_cube"
	},
	{
		"type": 49,
		"name": "Marker",
		"box_xz": "0.0",
		"box_y": "0.0",
		"ID": "minecraft:marker"
	},
	{
		"type": 50,
		"name": "Minecart",
		"box_xz": "0.98",
		"box_y": "0.7",
		"ID": "minecraft:minecart"
	},
	{
		"type": 51,
		"name": "Minecart Chest",
		"box_xz": "0.98",
		"box_y": "0.7",
		"ID": "minecraft:chest_minecart"
	},
	{
		"type": 52,
		"name": "Minecart Command Block",
		"box_xz": "0.98",
		"box_y": "0.7",
		"ID": "minecraft:commandblock_minecart"
	},
	{
		"type": 53,
		"name": "Minecart Furnace",
		"box_xz": "0.98",
		"box_y": "0.7",
		"ID": "minecraft:furnace_minecart"
	},
	{
		"type": 54,
		"name": "Minecart Hopper",
		"box_xz": "0.98",
		"box_y": "0.7",
		"ID": "minecraft:hopper_minecart"
	},
	{
		"type": 55,
		"name": "Minecart Spawner",
		"box_xz": "0.98",
		"box_y": "0.7",
		"ID": "minecraft:spawner_minecart"
	},
	{
		"type": 56,
		"name": "Minecart TNT",
		"box_xz": "0.98",
		"box_y": "0.7",
		"ID": "minecraft:tnt_minecart"
	},
	{
		"type": 57,
		"name": "Mule",
		"box_xz": "1.39648",
		"box_y": "1.6",
		"ID": "minecraft:mule"
	},
	{
		"type": 58,
		"name": "Mooshroom",
		"box_xz": "0.9",
		"box_y": "1.4",
		"ID": "minecraft:mooshroom"
	},
	{
		"type": 59,
		"name": "Ocelot",
		"box_xz": "0.6",
		"box_y": "0.7",
		"ID": "minecraft:ocelot"
	},
	{
		"type": 60,
		"name": "Painting",
		"box_xz": "type width or 0.0625 (depth)",
		"box_y": "type height",
		"ID": "minecraft:painting"
	},
	{
		"type": 61,
		"name": "Panda",
		"box_xz": "1.3",
		"box_y": "1.25",
		"ID": "minecraft:panda"
	},
	{
		"type": 62,
		"name": "Parrot",
		"box_xz": "0.5",
		"box_y": "0.9",
		"ID": "minecraft:parrot"
	},
	{
		"type": 63,
		"name": "Phantom",
		"box_xz": "0.9",
		"box_y": "0.5",
		"ID": "minecraft:phantom"
	},
	{
		"type": 64,
		"name": "Pig",
		"box_xz": "0.9",
		"box_y": "0.9",
		"ID": "minecraft:pig"
	},
	{
		"type": 65,
		"name": "Piglin",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:piglin"
	},
	{
		"type": 66,
		"name": "Piglin Brute",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:piglin_brute"
	},
	{
		"type": 67,
		"name": "Pillager",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:pillager"
	},
	{
		"type": 68,
		"name": "Polar Bear",
		"box_xz": "1.4",
		"box_y": "1.4",
		"ID": "minecraft:polar_bear"
	},
	{
		"type": 69,
		"name": "Primed TNT",
		"box_xz": "0.98",
		"box_y": "0.98",
		"ID": "minecraft:tnt"
	},
	{
		"type": 70,
		"name": "Pufferfish",
		"box_xz": "0.7",
		"box_y": "0.7",
		"ID": "minecraft:pufferfish"
	},
	{
		"type": 71,
		"name": "Rabbit",
		"box_xz": "0.4",
		"box_y": "0.5",
		"ID": "minecraft:rabbit"
	},
	{
		"type": 72,
		"name": "Ravager",
		"box_xz": "1.95",
		"box_y": "2.2",
		"ID": "minecraft:ravager"
	},
	{
		"type": 73,
		"name": "Salmon",
		"box_xz": "0.7",
		"box_y": "0.4",
		"ID": "minecraft:salmon"
	},
	{
		"type": 74,
		"name": "Sheep",
		"box_xz": "0.9",
		"box_y": "1.3",
		"ID": "minecraft:sheep"
	},
	{
		"type": 75,
		"name": "Shulker",
		"box_xz": "1.0",
		"box_y": "1.0-2.0 (depending on peek)",
		"ID": "minecraft:shulker"
	},
	{
		"type": 76,
		"name": "Shulker Bullet",
		"box_xz": "0.3125",
		"box_y": "0.3125",
		"ID": "minecraft:shulker_bullet"
	},
	{
		"type": 77,
		"name": "Silverfish",
		"box_xz": "0.4",
		"box_y": "0.3",
		"ID": "minecraft:silverfish"
	},
	{
		"type": 78,
		"name": "Skeleton",
		"box_xz": "0.6",
		"box_y": "1.99",
		"ID": "minecraft:skeleton"
	},
	{
		"type": 79,
		"name": "Skeleton Horse",
		"box_xz": "1.39648",
		"box_y": "1.6",
		"ID": "minecraft:skeleton_horse"
	},
	{
		"type": 80,
		"name": "Slime",
		"box_xz": "0.51000005 * size",
		"box_y": "0.51000005 * size",
		"ID": "minecraft:slime"
	},
	{
		"type": 81,
		"name": "Small Fireball",
		"box_xz": "0.3125",
		"box_y": "0.3125",
		"ID": "minecraft:small_fireball"
	},
	{
		"type": 82,
		"name": "Snow Golem",
		"box_xz": "0.7",
		"box_y": "1.9",
		"ID": "minecraft:snow_golem"
	},
	{
		"type": 83,
		"name": "Snowball",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:snowball"
	},
	{
		"type": 84,
		"name": "Spectral Arrow",
		"box_xz": "0.5",
		"box_y": "0.5",
		"ID": "minecraft:spectral_arrow"
	},
	{
		"type": 85,
		"name": "Spider",
		"box_xz": "1.4",
		"box_y": "0.9",
		"ID": "minecraft:spider"
	},
	{
		"type": 86,
		"name": "Squid",
		"box_xz": "0.8",
		"box_y": "0.8",
		"ID": "minecraft:squid"
	},
	{
		"type": 87,
		"name": "Stray",
		"box_xz": "0.6",
		"box_y": "1.99",
		"ID": "minecraft:stray"
	},
	{
		"type": 88,
		"name": "Strider",
		"box_xz": "0.9",
		"box_y": "1.7",
		"ID": "minecraft:strider"
	},
	{
		"type": 89,
		"name": "Thrown Egg",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:egg"
	},
	{
		"type": 90,
		"name": "Thrown Ender Pearl",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:ender_pearl"
	},
	{
		"type": 91,
		"name": "Thrown Expierience Bottle",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:experience_bottle"
	},
	{
		"type": 92,
		"name": "Thrown Potion",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:potion"
	},
	{
		"type": 93,
		"name": "Thrown Trident",
		"box_xz": "0.5",
		"box_y": "0.5",
		"ID": "minecraft:trident"
	},
	{
		"type": 94,
		"name": "Trader Llama",
		"box_xz": "0.9",
		"box_y": "1.87",
		"ID": "minecraft:trader_llama"
	},
	{
		"type": 95,
		"name": "Tropical Fish",
		"box_xz": "0.5",
		"box_y": "0.4",
		"ID": "minecraft:tropical_fish"
	},
	{
		"type": 96,
		"name": "Turtle",
		"box_xz": "1.2",
		"box_y": "0.4",
		"ID": "minecraft:turtle"
	},
	{
		"type": 97,
		"name": "Vex",
		"box_xz": "0.4",
		"box_y": "0.8",
		"ID": "minecraft:vex"
	},
	{
		"type": 98,
		"name": "Villager",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:villager"
	},
	{
		"type": 99,
		"name": "Vindicator",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:vindicator"
	},
	{
		"type": 100,
		"name": "Wandering Trader",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:wandering_trader"
	},
	{
		"type": 101,
		"name": "Witch",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:witch"
	},
	{
		"type": 102,
		"name": "Wither",
		"box_xz": "0.9",
		"box_y": "3.5",
		"ID": "minecraft:wither"
	},
	{
		"type": 103,
		"name": "Wither Skeleton",
		"box_xz": "0.7",
		"box_y": "2.4",
		"ID": "minecraft:wither_skeleton"
	},
	{
		"type": 104,
		"name": "Wither Skull",
		"box_xz": "0.3125",
		"box_y": "0.3125",
		"ID": "minecraft:wither_skull"
	},
	{
		"type": 105,
		"name": "Wolf",
		"box_xz": "0.6",
		"box_y": "0.85",
		"ID": "minecraft:wolf"
	},
	{
		"type": 106,
		"name": "Zoglin",
		"box_xz": "1.39648",
		"box_y": "1.4",
		"ID": "minecraft:zoglin"
	},
	{
		"type": 107,
		"name": "Zombie",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:zombie"
	},
	{
		"type": 108,
		"name": "Zombie Horse",
		"box_xz": "1.39648",
		"box_y": "1.6",
		"ID": "minecraft:zombie_horse"
	},
	{
		"type": 109,
		"name": "Zombie Villager",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:zombie_villager"
	},
	{
		"type": 110,
		"name": "Zombified Piglin",
		"box_xz": "0.6",
		"box_y": "1.95",
		"ID": "minecraft:zombified_piglin"
	},
	{
		"type": 111,
		"name": "Player",
		"box_xz": "0.6",
		"box_y": "1.8",
		"ID": "minecraft:player"
	},
	{
		"type": 112,
		"name": "Fishing Hook",
		"box_xz": "0.25",
		"box_y": "0.25",
		"ID": "minecraft:fishing_bobber"
	},
]

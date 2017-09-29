class Room():
	def __init__(self, room_name):
		self.name = room_name
		self.description = None
		self.linked_rooms = {}
		self.character = None
		self.item = None
		self.has_locked_door = False

	def set_description(self, room_description):
		self.description = room_description

	def get_description(self):
		return self.description

	def set_name(self, room_name):
		self.name = room_name

	def get_name(self):
		return self.name

	def describe(self):
		print(self.description)
		
	def get_character(self):
		return self.character
		
	def set_character(self, character_in_room):
		self.character = character_in_room
		
	def get_item(self):
		return self.item
		
	def set_item(self, room_item):
		self.item = room_item

	def link_room(self, room_to_link, direction):
		self.linked_rooms[direction] = room_to_link
		# print(self.name + " linked rooms: " + repr(self.linked_rooms))

	def display_details(self):
		title = "The " + self.get_name()
		print(title)
		print('-' * len(title))
		print(self.get_description())
		for direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			if room == None:
                                continue
			print("The " + room.get_name() + " is " + direction)
		print()

	def move(self, direction):
		if self.linked_rooms[direction].name == "Conservatory" and self.has_locked_door:
			print("A whirlwind of icy air throws you back. Cora glares at you.")
			return self
		if direction in self.linked_rooms:
			return self.linked_rooms[direction]
		else:
			print("You can't go that way")
			return self

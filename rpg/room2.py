class Room():
	def __init__(self, room_name):
		self.name = room_name
		self.description = None
		self.linked_rooms = {}
		self.character = None
		self.item = None
		self.blocked_exit = None
		
	def set_name(self, room_name):
		"""room_name is a string representing the name of the room."""
		self.name = room_name

	def get_name(self):
		"""Returns the name of the room as a string."""
		return self.name

	def set_description(self, room_description):
		"""room_description is a string describing the room."""
		self.description = room_description

	def get_description(self):
		"""Returns a string describing the room."""
		return self.description

	def describe(self):
		"""Prints a string describing the room."""
		print(self.description)

	def link_room(self, room_to_link, direction):
		"""Adds to a dictionary of the form {"west": ballroom}
		   in which case, the command "west" moves the player
		   to the ballroom.
		"""
		self.linked_rooms[direction] = room_to_link
		
	def get_character(self):
		"""Returns a Character object. There is a maximum of one character
		   per room.
		"""
		return self.character
		
	def set_character(self, character_in_room):
		"""character_in_room is a Character object. There is a maximum of
		   one character per room.
		"""
		self.character = character_in_room
		
	def get_item(self):
		"""Returns an Item object. There is a maximum of one item per room."""
		return self.item
		
	def set_item(self, room_item):
		"""room_item is an Item object. There is a maximum of
		   one item per room.
		"""
		self.item = room_item
		
	def set_blocked_exit(self, direction, message):
		"""This is used when a link to another room exists, but 
		   the player must be prevented from going that way.
		   direction is a string, e.g. "west"
		   message is a string e.g. "The guard won't let you pass."
		"""
		self.blocked_exit = {direction: message}

	def display_details(self):
		"""Prints the name and description of the room, 
		   and details of the exits to other rooms.
		"""
		title = "The " + self.get_name()
		print(title)
		print('-' * len(title))
		print(self.get_description() + "\n")
		for direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			if room == None:
				continue
			print("The " + room.get_name() + " is " + direction)
		print()

	def move(self, direction):
		"""direction is a string, e.g. "west"
		   If there is no exit in that direction, or the exit is blocked,
		   print a message, and return the current Room object.
		   Otherwise, return the Room object for that direction.
		"""
		if self.blocked_exit is not None and direction in self.blocked_exit:
			print(self.blocked_exit[direction])
			return self
		elif direction in self.linked_rooms:
			return self.linked_rooms[direction]
		else:
			print("You can't go that way")
			return self

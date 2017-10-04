class Character():

	# Create a character
	def __init__(self, char_name, char_description):
		self.name = char_name
		self.description = char_description
		self.owns = None				# Item object
		self.conversation = None		# string
		self.says = {}					# dictionary  {topic: conversation}
		
	


	# Set what this character will say when talked to
	def set_conversation(self, conversation):
		"""conversation is a string representing one reply from the character."""
		self.conversation = conversation
		
	# Set an Item object that this character owns
	def set_owns(self, item_object):
		"""item_object is an Item object.
		   A character can own an item regardless of where the item is.
		"""
		self.owns = item_object

	# Describe this character
	def describe(self):
		"""Prints the name and description of the character."""
		print( self.name + " is here!" )
		print( self.description, end="\n\n" )

	# Talk to this character
	def talk(self):
		"""Prints the character's conversation, or, if none exists,
		   prints a default message.
		 """
		if self.conversation is not None:
			print("[" + self.name + " says]: " + self.conversation)
		else:
			print(self.name + " doesn't want to talk to you")			
			
	# Fight with this character
	def fight(self, combat_item):
		"""Prints a default message and returns True"""
		print(self.name + " doesn't want to fight with you")
		return True
		
	# Give something to this character
	def give(self, gift_item, current_room):
		"""Prints a default message."""
		print(self.name + " doesn't want anything.")
		
	# Hug character
	def hug(self):
		"""Prints a default message."""
		print(self.name + " looks surprised.")



class Enemy(Character):
	
	combat_wins = 0		# The number of times the character has won a fight.
	
	def __init__(self, char_name, char_description):
		# to make an Enemy, first make a Character object
		# and then we'll customise it.
		super().__init__(char_name, char_description)
		self.weakness = None						# Item object
		self.defeats = 0
		self.attack_moves = None					# List of strings
		self.post_attack = None						# Dict {defeat_num : message}
		self.wants = None							# Item object
		self.alter_ego = None						# Character object
		
	def get_wants(self):
		"""Returns an Item object (the item the character wants)"""
		return self.wants
		
	def set_wants(self, char_wants):
		"""char_wants is an Item object (the item the character wants)"""
		self.wants = char_wants
		
	def get_alter_ego(self):
		"""Returns a Character object, representing the current 
		   character after being changed by a command.
		"""
		return self.alter_ego
		
	def set_alter_ego(self, character):
		"""character is a Character object, representing the current
		   character after being changed by a command.
		"""
		self.alter_ego = character

	def get_weakness(self):
		"""Returns an Item object, representing the weapon 
		   that defeats the character in a fight.
		"""
		return self.weakness

	def set_weakness(self, char_weakness):
		"""char_weakness is an Item object, representing the weapon
		   that defeats the character in a fight.
		"""
		self.weakness = char_weakness
		
	def set_attack_moves(self, list_of_moves):
		"""list_of_moves is a list of strings describing how the character 
		   attacks. One message will be printed before each round of combat.
		"""
		self.attack_moves = list_of_moves
		
	def set_post_attack(self, defeat_num, message):
		"""Adds to a dictionary for which the keys (defeat_num) are integers 
		   representing the number of times the character has been defeated, 
		   and the values (message) are strings describing the character's
		   reaction following combat.
		"""
		if self.post_attack == None:
			self.post_attack = {}
		self.post_attack[defeat_num] = message
		
	def give(self, gift_item, current_room):
		"""  gift_item is an Item object, current_room is the current Room object.
		     Prints an appropriate message.
		     An accepted gift has the effect of switching the current character
		   with another Character object if one is defined in self.alter_ego).
		     Returns True if the gift is accepted, otherwise False.
		 """
		if self.wants.get_name() == gift_item:
			if self.alter_ego is not None:
				# Correct gift changes character into alter_ego
				current_room.set_character(self.alter_ego)
			print(self.name + " is delighted with the " + gift_item + ".")
			return True
		else:
			print(self.name + " angrily rejects the " + gift_item + ".")
			return False

	def fight(self, combat_item):
		"""  combat_item is a string representing the name of an Item object.
		     If defined, print the pre-fight message corresponding to the 
		   current number of character defeats.
		     Print a description of the fight being won or lost.
		     If defined, print the after-fight message corresponding to the
		   updated number of character defeats.
		     Return True if the player wins, otherwise False.
		"""
		if self.attack_moves is not None and self.defeats < len(self.attack_moves):
			print("\n" + self.name + " " + self.attack_moves[self.defeats] + "\n")
			
		if self.weakness.get_name() == combat_item:
			print("You fend " + self.name + " off with the " + combat_item + ".")
			self.defeats += 1
			# if a message is linked to this number of defeats, print it.
			if self.post_attack is not None and self.defeats in self.post_attack:
				print("\n" + self.post_attack[self.defeats])
			return True
			
		else:
			print(self.name + " crushes you, puny adventurer")
			return False

		
class Friend(Character):
	def __init__(self, char_name, char_description):
		# To make a Friend, first make a Character object
		# and then we'll customise it.
		super().__init__(char_name, char_description)
		
	def hug(self):
		"""Print a default message."""
		print(self.name + " happily hugs you back.")


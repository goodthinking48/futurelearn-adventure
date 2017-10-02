class Character():

	# Create a character
	def __init__(self, char_name, char_description):
		self.name = char_name
		self.description = char_description
		self.owns = None				# Item object
		self.conversation = None		# string
		self.says = {}					# dictionary = {topic: conversation}

	# Describe this character
	def describe(self):
		print( self.name + " is here!" )
		print( self.description, end="\n\n" )

	# Set what this character will say when talked to
	def set_conversation(self, conversation):
		self.conversation = conversation
		
	# Set an Item object that this character owns
	def set_owns(self, item_object):
		self.owns = item_object

	# Talk to this character
	def talk(self):
		if self.conversation is not None:
			print("[" + self.name + " says]: " + self.conversation)
		else:
			print(self.name + " doesn't want to talk to you")
			
			
	# Fight with this character
	def fight(self, combat_item):
		print(self.name + " doesn't want to fight with you")
		return True
		
	# Give something to this character
	def give(self, gift_item, current_room):
		print(self.name + " doesn't want anything.")
		
	# Hug character
	def hug(self):
		print(self.name + " looks surprised.")



class Enemy(Character):
	
	combat_wins = 0
	
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
		return self.wants
		
	def set_wants(self, char_wants):
		self.wants = char_wants
		
	def get_alter_ego(self):
		return self.alter_ego
		
	def set_alter_ego(self, character):
		self.alter_ego = character

	def get_weakness(self):
		return self.weakness

	def set_weakness(self, char_weakness):
		self.weakness = char_weakness
		
	def set_attack_moves(self, list_of_moves):
		self.attack_moves = list_of_moves
		
	def set_post_attack(self, defeat_num, message):
		# defeat_num is an integer (the updated number of defeats)
		if self.post_attack == None:
			self.post_attack = {}
		self.post_attack[defeat_num] = message
		
	def give(self, gift_item, current_room):
		# gift_item is a string.
		if self.wants.get_name() == gift_item:
			if self.alter_ego is not None:
				# Correct gift changes character into alter-ego
				current_room.set_character(self.alter_ego)
			print(self.name + " is delighted with the " + gift_item + ".")
			return True
		else:
			print(self.name + " angrily rejects the " + gift_item + ".")
			return False

	def fight(self, combat_item):
		# combat_item is a string
		# if an attack is described for this number of defeats, print it.
		if self.attack_moves is not None and self.defeats < len(self.attack_moves):
			print("\n" + self.name + " " + self.attack_moves[self.defeats] + "\n")
			
		if self.weakness.get_name() == combat_item:
			print("You fend " + self.name + " off with the " + combat_item + ".")
			self.defeats += 1
			# if a message is linked to this number of defeats, print it.
			if self.post_attack is not None and self.defeats in self.post_attack:
				print("\n" + self.post_attack[self.defeats] +"\n")
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
		print(self.name + " happily hugs you back.")


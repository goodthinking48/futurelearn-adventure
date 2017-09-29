class Character():

	# Create a character
	def __init__(self, char_name, char_description):
		self.name = char_name
		self.description = char_description
		self.conversation = None

	# Describe this character
	def describe(self):
		print( self.name + " is here!" )
		print( self.description, end="\n\n" )

	# Set what this character will say when talked to
	def set_conversation(self, conversation):
		self.conversation = conversation

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
	def give(self, gift_item):
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
		self.weakness = None					# Item object
		self.defeats = 0
		self.wants = None							# Item object
		self.friendly_character = None				# Character object
		
	def get_wants(self):
		return self.wants
		
	def set_wants(self, char_wants):
		self.wants = char_wants
		
	def get_friendly_character(self):
		return self.friendly_character
		
	def set_friendly_character(self, character):
		self.friendly_character = character

	def get_weakness(self):
		return self.weakness

	def set_weakness(self, char_weakness):
		self.weakness = char_weakness
		
	def give(self, gift_item):
		# gift_item is a string
		if self.wants.get_name() == gift_item:
			print(self.name + " is delighted with the " + gift_item + ".")
			return True
		else:
			print(self.name + " angrily rejects the " + gift_item + ".")
			return False

	def fight(self, combat_item):
		# combat_item is a string
		if self.weakness.get_name() == combat_item:
			print("You fend " + self.name + " off with the " + combat_item + ".")
			self.defeats += 1
			Enemy.combat_wins += 1
			return True
		else:
			print(self.name + " crushes you, puny adventurer")
			return False

		
class Friend(Character):
	def __init__(self, char_name, char_description):
		# to make a Friend, first make a Character object
		# and then we'll customise it.
		super().__init__(char_name, char_description)
		
	def hug(self):
		print(self.name + " happily hugs you back.")


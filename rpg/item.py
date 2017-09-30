class Item():
	def __init__(self, item_name, item_description):
		self.name = item_name
		self.description = item_description
		self.smell = None
		self.owner = None
		self.is_edible = False

	def get_description(self):
		return self.description

	def set_description(self, item_description):
		self.description = item_description

	def get_name(self):
		return self.name

	def set_name(self, item_name):
		self.name = item.name

	def get_smell(self):
		if self.smell == None:
			return "It doesn't really smell of anything."
		else:
			return self.smell

	def set_smell(self, item_smell):
		self.smell = item_smell
		
	def set_edibility(self, edible=False):
		self.is_edible = edible
		
	def get_owner(self):
		return self.owner
		
	def set_owner(self, character):
		self.owner = character
		
	def eat_it(self, backpack):
		if self.is_edible:
			print("Delicious!")
			backpack.remove(self.get_name())
		else:
			print("You can't eat that!")
		return backpack
		
	def smell_it(self):
		print(self.get_smell())

	def describe(self):
		print("You see: " + self.get_description(), end="\n\n")

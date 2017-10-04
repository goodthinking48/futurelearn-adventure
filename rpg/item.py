class Item():
	def __init__(self, item_name, item_description):
		self.name = item_name
		self.description = item_description
		self.smell = None					# String describes smell
		self.alternative = None				# Item object

	def get_name(self):
		"""Returns the name of the item as a string."""
		return self.name

	def set_name(self, item_name):
		"""item_name is the name of the item as a string"""
		self.name = item.name
		
	def get_description(self):
		"""Returns the description of the item as a string."""
		return self.description

	def set_description(self, item_description):
		"""item_description is the description of the item as a string"""
		self.description = item_description

	def get_smell(self):
		"""Returns the smell description as a string, or a default message"""
		if self.smell == None:
			return "It doesn't really smell of anything."
		else:
			return self.smell

	def set_smell(self, item_smell):
		"""item_smell is a string describing the smell."""
		self.smell = item_smell
		
	def get_alternative(self):
		"""Returns another Item object, which represents the
		   current item after a command has changed it.
		"""
		return self.alternative
		
	def set_alternative(self, alternative):
		"""alternative is another Item object, which represents the
		   current item after a command has changed it.
		"""
		self.alternative = alternative
		
	def eat_it(self, backpack):
		"""If there is "cheese" in the backpack (a list of item names),
		   print a message and remove it, else print a default message.
		   Returns the backpack.
		"""
		if "cheese" in backpack:
			print("Delicious!")
			backpack.remove("cheese")
		else:
			print("You don't have any food.")
		return backpack
		
	def smell_it(self, current_room):
		"""Prints the smell of the item."""
		print(self.get_smell())

	def describe(self):
		"""Prints the description of the item."""
		print("You see: " + self.get_description(), end="\n\n")

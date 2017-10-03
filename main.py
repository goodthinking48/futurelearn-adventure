
from setup import *


backpack = []
current_room = dining_hall

print("\n\n" + "Welcome to the Haunted House!" + "\n")
print("Available commands are: eat, fight, give, hug, smell, take, talk")
print("Also: north, south, east, west")
print("Also: quit or q" + "\n")
print("Not all items and conversations are useful, but most are,")
print("and Teddy has good advice in several situations." + "\n")
print("You win by finding the treasure vault (or by fighting a lot)." + "\n")
print("'...' means 'Press Enter to continue.'"  "\n")
input("...")



while True:

	# Display room and contents
	print("\n")
	current_room.display_details()
	
	room_item = current_room.get_item()
	if room_item is not None:
		room_item.describe()

	inhabitant = current_room.get_character()
	if inhabitant is not None:
		inhabitant.describe()
		
	if len(backpack) > 0:
		carried_items = ", ".join(backpack)
		print("In your backpack: " + carried_items, end="\n\n")
		


	command = input("> ").lower()
	
	# Deal with missing items and characters
	if command in ['hug', 'talk', 'give', 'fight'] and inhabitant == None:
		print("There's no-one here.")
		continue
		
	if command in ['smell', 'take', 'get'] and room_item == None:
		print("There's nothing to " + command + " here.")
		continue
		
	if command in ['eat', 'give'] and len(backpack) == 0:
		print("You don't have anything to " + command + ".")
		continue
	
	
	
	# Run commands
	if command in ["north", "south", "east", "west"]:
		current_room = current_room.move(command)

		
	elif command == "take" or command == "get":
		backpack.append(room_item.get_name())
		current_room.set_item(None)

	
	elif command == "talk":
		inhabitant.talk()
		if inhabitant == cora_friend:
			# Cora says thank you by opening the vault
			dining_hall.link_room(vault, "south")
			
			
	elif command == "hug":
		inhabitant.hug()
		
		
	elif command == "give":
		gift = input("What do you want to give? ")
		if gift not in backpack:
			print("You haven't got that.")
			continue
		gift_liked = inhabitant.give(gift, current_room)
		if gift_liked:
			backpack.remove(gift)
			if gift == "diamond" and inhabitant == cora:
				cora_friend.owns = diamond
						
			
	elif command == "fight":
		weapon = input("What do you want to fight with? ")
		if weapon not in backpack:
			print("You don't have that!")
			continue
		fight_won = inhabitant.fight(weapon)
		
		if not fight_won:
			print("\n" + "Game over!" + "\n")
			break
		if inhabitant == cora and inhabitant.defeats == 1:
			ballroom.has_blocked_door = False
			backpack.remove("torch")
		if inhabitant.owns == diamond and inhabitant.defeats == 4:
			print("Something glitters as it falls to the floor.")
			current_room.set_item(diamond)
			inhabitant.owns = None
		if inhabitant == davos and inhabitant.defeats == 5:
			current_room.set_character(None)
			terrace.set_character(davos)
			print("You have won the game by defeating the zombie butler!", end="\n\n")
			print("(You can still find the treasure...)")
			
			
	elif command == "eat":
		backpack = cheese.eat_it(backpack)
			
				
	elif command =="smell":
		room_item.smell_it(current_room)
	
	
	elif command in ["quit", "q"]:
		break
		
		
	else:
		print("I don't understand.")
		
		
		
	# Set Teddy's advice
	if cora.defeats > 0:
		teddy.set_conversation(teddy.says["davos"])
	if "diamond" in backpack:
		teddy.set_conversation(teddy.says["diamond"])
	if cora_friend.owns == diamond:
		teddy.set_conversation(teddy.says["thanks"])
	if "south" in dining_hall.linked_rooms:
		teddy.set_conversation(teddy.says["treasure"])
		
		
	
	# Wait for input to allow previous activity to be read.
	if command in ["eat", "fight", "give", "hug", "smell", "talk"]:
		input("...")
	elif current_room == ballroom and ballroom.has_blocked_door and command == "north":
		input("...")
		
		
		
	# The game is won by reaching the vault.					
	if current_room == vault:
		print("You have won the game by finding the treasure!" + "\n")
		break

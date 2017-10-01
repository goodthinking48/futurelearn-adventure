
from setup import *


backpack = []
current_room = dining_hall
command = ""

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
	
	# Wait for input to allow previous activity to be read.
	if command in ["eat", "fight", "give", "hug", "smell", "talk"]:
		input("...")
	elif current_room == ballroom and ballroom.has_blocked_door and command == "north":
		input("...")


	# Display room and contents
	print("\n")
	current_room.display_details()						
	if current_room == vault:						# to do: move
		print("You have won the game by finding the treasure!" + "\n")
		break
	
	room_item = current_room.get_item()
	if room_item is not None:
		room_item.describe()

	inhabitant = current_room.get_character()
	if inhabitant is not None:
		inhabitant.describe()
		
	if len(backpack) > 0:
		carried_item_list = ", ".join(backpack)
		print("In your backpack: " + carried_item_list, end="\n\n")
		
		
	# Set Teddy's advice
	if ballroom.has_blocked_door == False:
		teddy.set_conversation(teddy.says["davos"])
	if diamond.get_owner() == None:
		teddy.set_conversation(teddy.says["diamond"])
	if diamond.get_owner() == cora_friend:
		teddy.set_conversation(teddy.says["thanks"])
	if "south" in dining_hall.linked_rooms:
		teddy.set_conversation(teddy.says["treasure"])


	# Get command and deal with common mistakes
	command = input("> ").lower()
	
	if command in ['hug', 'talk', 'give', 'fight'] and inhabitant == None:
		print("There's no-one here.")
		continue
		
	if command in ['smell', 'take', 'get'] and room_item == None:
		print("There's nothing to " + command + " here.")
		continue
		
	if command in ['eat'] and len(backpack) == 0:
		print("You don't have anything to " + command + ".")
		continue
	
	
	# Run commands
	if command in ["north", "south", "east", "west"]:
		current_room = current_room.move(command)

		
	elif command == "take" or command == "get":
		backpack.append(room_item.get_name())
		current_room.set_item(None)

	
	elif command == "talk":
		consequence = inhabitant.talk()
		if consequence == "Cora opens the vault":
			pass		# move vault opening code here
			
			
	elif command == "hug":
		inhabitant.hug()
		
		
	elif command == "give":
		gift = input("What do you want to give? ")
		if gift not in backpack:
			print("You haven't got that.")
			continue
		gift_liked = inhabitant.give(gift)
		if gift_liked:
			backpack.remove(gift)
			if inhabitant == cora:
				ballroom.has_blocked_door = False
				diamond.set_owner(cora_friend)
		if gift_liked and inhabitant.friendly_character is not None:
			current_room.set_character(inhabitant.friendly_character)
			
			
	elif command == "fight":
		weapon = input("What do you want to fight with? ")
		if weapon not in backpack:
			print("You don't have that!")
			continue
		fight_won = inhabitant.fight(weapon)
		if not fight_won:
			print("\n" + "Game over!" + "\n")
			break
		if inhabitant == cora:
			print("\n" + "The torch flies from your hand and shatters on the floor.")
			print("Cora swirls away to the other side of the room.")
			ballroom.has_blocked_door = False
			backpack.remove("torch")
		if inhabitant == davos and inhabitant.defeats == 4:
			print("Davos trips on the broom and flies head over heels." + "\n")
		if inhabitant == diamond.get_owner() and inhabitant.defeats == 4:
			print("Something glitters as it falls to the floor.")
			current_room.set_item(diamond)
			diamond.set_owner(None)
		if inhabitant == davos and inhabitant.defeats == 5:
			print("\n" + "Davos fixes you with a look of withering contempt, before" + "\n" +
			      "hauling himself off to the terrace for a nice rest." + "\n")
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

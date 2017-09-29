
from setup import *
from time import sleep


backpack = []
current_room = dining_hall
command = ""

print("\n\n" + "Welcome to the Haunted House!" + "\n")
print("Available commands are: eat, fight, give, hug, smell, take, talk")
print("Also: north, south, east, west")
print("Also: quit or q" + "\n")
print("Not all items and conversations are useful, but most are." + "\n")
print("You win by finding the treasure vault (or by fighting a lot)." + "\n")
print("'...' means 'Press Enter to continue.'"  "\n")
input("...")



while True:
	
	if command in ["eat", "fight", "give", "hug", "smell", "talk"]:
		input("...")
	elif current_room == ballroom and ballroom.has_locked_door and command == "north":
		input("...")

	print("\n")
	current_room.display_details()
	if current_room == vault:
		print("You have found the treasure! You have won.")
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
		
	command = input("> ").lower()
	
	if command in ["north", "south", "east", "west"]:
		current_room = current_room.move(command)

		
	elif command == "take" or command == "get":
		if room_item is not None:
			backpack.append(room_item.get_name())
			current_room.set_item(None)
		else:
			print("I don't see that here.")
		
	elif (command in ["talk", "hug", "give", "fight"] and
		  inhabitant is not None):
		if command == "talk":
			inhabitant.talk()
			if inhabitant == cora_friend:
				dining_hall.link_room(vault, "south")
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
					ballroom.has_locked_door = False
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
				ballroom.has_locked_door = False
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
		if "cheese" in backpack:
			print("Delicious!")
			backpack.remove("cheese")
		else:
			print("You haven't got any food.")
				
	elif command =="smell":
		if room_item is not None:
			print(room_item.get_smell())
			if room_item == orchid:
				current_room.set_item(hyacinth)
				room_item = hyacinth
		else:
			print("You cant't smell anything much.")
	
	elif command in ["quit", "q"]:
		break
	else:
		print("I don't understand.")

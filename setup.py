import rpg

# Items (location is set in the Room object)
broom = rpg.Item("broom", "A long, bristly broom.")
broom.set_smell("The broom smells of pine and rosemary.")

cheese = rpg.Item("cheese", "A nice bit of crumbly cheese.")
cheese.set_smell("The cheese smells sharp and fresh.")

diamond = rpg.Item("diamond", "A tiny, sparkling diamond.")

orchid = rpg.Item("orchid", "A rare, blue orchid - very pretty.")

torch = rpg.Item("torch", "An ultra-bright electric torch.")


# Characters
davos = rpg.Enemy("Davos", "An ancient and crumbling butler.")
davos.set_conversation("Brrlgrh... rgrhl... brains..." +
                       "\n" + "(Oh dear!)")
davos.set_weakness(broom)
davos.set_wants(cheese)
diamond.set_owner(davos)

cora_friend = rpg.Friend("Cora", "A blithe spirit.")
cora_friend.set_conversation("I've opened the secret vault - have a look!")

cora = rpg.Enemy("Cora", "The restless, ghostly presence of a young lady.")
cora.set_conversation("Thief! Give me back my diamond!")
cora.set_friendly_character(cora_friend)
cora.set_weakness(torch)
cora.set_wants(diamond)

teddy = rpg.Friend("Teddy", "A small, friendly bear cub, with soft brown fur.")
teddy_says = "This house is haunted ... the ghost of Lady Cora is in the ballroom."
teddy_says += "\n" + "And she's angry! I don't know why. But don't worry, "
teddy_says += "bright lights scare her."
teddy.set_conversation(teddy_says)

# Rooms
kitchen = rpg.Room("Kitchen")
kitchen.set_description("A pretty and clean room in the farmhouse style.")
kitchen.set_character(davos)
kitchen.set_item(broom)

dining_hall = rpg.Room("Dining Hall")
dining_hall.set_description("A long, high-ceilinged room panelled in oak.")
dining_hall.set_character(teddy)

ballroom = rpg.Room("Ballroom")
ballroom.set_description("A vast, echoing space, with splendid golden decorations.")
ballroom.set_character(cora)

pantry = rpg.Room("Pantry")
pantry.set_description("Cool, shaded storage.")
pantry.set_item(cheese)

broom_cupboard = rpg.Room("Broom Cupboard")
broom_cupboard.set_description("A tight space.")
broom_cupboard.set_item(torch)

vault = rpg.Room("Secret Passageway")
vault.set_description("A dead end. This tiny room is full of gold and jewels!")

conservatory = rpg.Room("Conservatory")
conservatory.set_description("Palm fronds and flowers fill this decorative glass-house.")
conservatory.set_item(orchid)

broom_cupboard.link_room(kitchen, "west")
kitchen.link_room(broom_cupboard, "east")

pantry.link_room(kitchen, "east")
kitchen.link_room(pantry, "west")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

conservatory.link_room(ballroom, "east")
ballroom.link_room(conservatory, "west")

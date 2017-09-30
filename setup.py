import rpg

# Items (location is set in the Room object)
broom = rpg.Item("broom", "A long, bristly broom.")
broom.set_smell("The broom smells of pine and rosemary.")

cheese = rpg.Item("cheese", "A nice bit of crumbly cheese.")
cheese.set_smell("The cheese smells sharp and fresh.")
cheese.set_edibility(True)

diamond = rpg.Item("diamond", "A tiny, sparkling diamond.")

orchid = rpg.Item("orchid", "A rare, indigo-blue orchid - very pretty.")
orchid.set_smell("A strong, sweet scent. " + "\n" +
                 "Ohhhhhhhh... my mistake, it's a hyacinth.")
hyacinth = rpg.Item("hyacinth", "A common hyacinth.")
hyacinth.set_smell("A strong, sweet scent.")

torch = rpg.Item("torch", "An ultra-bright electric torch.")


# Characters
davos = rpg.Enemy("Davos", "An ancient and crumbling butler.")
davos.set_conversation("Brrlgrh... rgrhl... brains..." +
                       "\n" + "(Oh dear, Davos doesn't sound too well. Best " +
                         "keep your distance.)")
davos.set_attack_moves(["lurches forward, arms outstretched.",
                        "thrashes around the room, punching everything in his path.",
                        "wobbles mightily, before trying to kill you again.",
                        "throws himself forward once more.",
                        "is still flat on his back from last time, but seizes" + "\n" +
                        "his chance to grab you by the ankle and try to eat your foot."])
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
teddy_says = ["This house is haunted... " + "\n" +
              "Watch out for Lady Cora's ghost! She's angry! I don't know why." + "\n" +
              "But don't worry, bright lights scare her.",
              "If you want to fight the butler, " + "\n" +
              "you'll need a weapon with a good long handle.",
              "Talk to Cora - she wants to say thank you.",
              "Well done! Now have a look at that treasure!"]
teddy.set_conversation(teddy_says[0])

# Rooms
kitchen = rpg.Room("Kitchen")
kitchen.set_description("A spotlessly clean room, big enough for forty cooks.")
kitchen.set_character(davos)

dining_hall = rpg.Room("Dining Hall")
dining_hall.set_description("A long, high-ceilinged room panelled in oak.")
dining_hall.set_character(teddy)

ballroom = rpg.Room("Ballroom")
ballroom.set_description("A vast room with a shining floor and splendid golden decorations.")
ballroom.has_locked_door = True
ballroom.set_character(cora)

pantry = rpg.Room("Pantry")

pantry.set_description("Cool, shaded storage for food.")
pantry.set_item(cheese)

broom_cupboard = rpg.Room("Broom Cupboard")
broom_cupboard.set_description("A tight space.")
broom_cupboard.set_item(torch)

vault = rpg.Room("Secret Passageway")
vault.set_description("A dead end. This tiny room is full of gold and jewels!")

conservatory = rpg.Room("Conservatory")
conservatory.set_description("Palm fronds and flowers fill this decorative glass-house.")
conservatory.set_item(orchid)

terrace = rpg.Room("Terrace")
terrace.set_description("Just outside the house, a little viewing terrace with a stone balustrade." + "\n" +
                        "Beyond you see rose gardens, deer parks, fountains, peacocks etc, etc, etc.")
terrace.set_item(broom)

broom_cupboard.link_room(kitchen, "west")
kitchen.link_room(broom_cupboard, "east")

pantry.link_room(kitchen, "east")
kitchen.link_room(pantry, "west")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

conservatory.link_room(ballroom, "south")
ballroom.link_room(conservatory, "north")

terrace.link_room(conservatory, "south")
conservatory.link_room(terrace, "north")

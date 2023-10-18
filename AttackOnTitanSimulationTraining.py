# Cary Dakota Wolfe
# IT140
# 12/9/2022

def main():
    rooms = {   # dictionary containing locations and directions
        'Shinganshina District': {'East': 'Trost District'},
        'Trost District': {'North': 'Utopia District', 'South': 'Karanes District',
                           'West': 'Shinganshina District', 'East': 'Orvud District',
                           'Item': 'Maneuver Gear'},
        'Utopia District': {'East': 'Stohess District', 'South': 'Trost District', 'Item': 'Rifle'},
        'Karanes District': {'East': 'Yarckel District', 'North': 'Trost District', 'Item': 'Flare Gun'},
        'Yarckel District': {'West': 'Karanes District', 'Item': 'Left Handed Sword'},
        'Stohess District': {'West': 'Utopia District', 'Item': 'Right Handed Sword'},
        'Orvud District': {'West': 'Trost District', 'North': 'Mitras', 'Item': 'Titan Injection'},
        'Mitras': {'South': 'Orvud District'}
    }

    current_location = 'Shinganshina District'    # creates all necessary variables
    user_direction = ''
    user_decision = ''
    inventory = []
    are_you_sure = ''
    try_again = ' '
    trost_scavenge = 0   # ensures opening dialogue for searching an area does not repeat upon second search
    utopia_scavenge = 0
    karanes_scavenge = 0
    yarckel_scavenge = 0
    stohess_scavenge = 0
    orvud_scavenge = 0
    maneuver_gear = ''
    rifle = ''
    flare_gun = ''
    l_sword = ''
    r_sword = ''
    titan_injection = ''


    print("CHAPTER 0 - Introduction")
    print("Welcome to the Paradis Titan attack simulation!!! (Press enter to progress dialogue)")
    print("In this simulation you will placed in a Titan attack scenario.")
    print("This scenario places you in the outer most district, Shinganshina, of our wonderful island, Paradis.")
    input()
    print("The walls that protect this district, and all of the others on Paradis have been breached by titans!!!")
    print("To survive this simulation you must navigate all of the open districts,")
    print("collect any available resources, and make your way to the safe haven of Paradis, the capital city, Mitras.")
    input()
    print("INTRODUCTORY MESSAGE CONCLUDED")
    input()
    print("Simulation initiated...")
    print("Good luck!!!\n")
    input()
    print("You are now in Shinganshina District.\n")
    input()
    print("Titans... are everywhere...")
    input()
    print("Everything is destroyed... there doesn't seem to be anything worth value here.")
    input()
    print("Shinganshina district is the outermost district in Paradis so it makes sense that it got hit the worst.")
    input()
    print("I need to get out of here as soon as possible, but the instructions said to look for resources.\n")
    print("What should I do?")
    print("1: Scavenge\n2: Get out of here\n")
    user_choice1 = input()
    loop_exit = ''
    while loop_exit != "Exit":
        if user_choice1 == "1":
            print("I need to find something useful.")
            input()
            print("I won't survive out here with nothing.")
            input()
            print("You begin scavenging the immediate area.")
            input()
            print("Nothing useful so far... just rubble!!!")
            input()
            print("Come on, there has to be something!!!")
            input()
            print("As you continue digging you feel a large dark shadow cast over you.")
            input()
            print("Before you can think to turn around, you're lifted off of the ground...")
            input()
            print("...face-to-face with a Titan at least 20 meters tall.")
            input()
            print("The titan lifts you towards their mouth, bites down on your neck, ")
            print("and rips your head clean off, before devouring the rest of your body.")
            input()
            print("SIMULATION FAILED.\n")
            print("Try again? ('Y' for yes, any other entry will exit.)")
            are_you_sure = input()
            if are_you_sure == 'Y' or '\n':
                print("1: Scavenge\n2: Get out of here\n")
                user_choice1 = input()
            else:
                loop_exit = "Exit"
                user_decision = 'Exit'

        elif user_choice1 == "2":
            print("You turn towards the closest district, and run as fast as you possibly can.")
            input()
            print("After running for what seems like forever you arrive at a battered sign which reads...")
            print("'TROST DISTRICT'")
            input()
            print("By some sort of miracle it seems like you've made it to the next district.")
            input()
            print("However, this district doesn't appear to be in good condition either.\n")
            input()
            print("CHAPTER 1: THE SIMULATION BEGINS\n")
            loop_exit = "Exit"
        else:
            print("Invalid entry.")
            print("1: Scavenge\n2: Get out of here\n")
            user_choice1 = input()

    while user_decision != 'Exit':  # maintains loop until exit is typed
        print("What would you like to do?\n")
        print("(Enter a listed direction ('East') to travel to the corresponding location('Trost District').)")
        print("(Type 'Scavenge' to search for the item hidden in the district.)")
        print("(Type 'Inventory' to check your collected items.)")
        print("(Type 'Exit' to exit the simulation.)\n")
        print("Current location:", current_location)  # presents current location to user

        if current_location == 'Shinganshina District':  # presents the items, rooms, and their corresponding directions
            print(rooms['Shinganshina District'], '\n')
        elif current_location == 'Trost District':
            print(rooms['Trost District'], '\n')
        elif current_location == 'Utopia District':
            print(rooms['Utopia District'], '\n')
        elif current_location == 'Karanes District':
            print(rooms['Karanes District'], '\n')
        elif current_location == 'Yarckel District':
            print(rooms['Yarckel District'], '\n')
        elif current_location == 'Stohess District':
            print(rooms['Stohess District'], '\n')
        elif current_location == 'Orvud District':
            print(rooms['Orvud District'], '\n')
        elif current_location == 'Mitras':
            print(rooms['Mitras'], '\n')

        user_direction = input()
        print('\n')   # user inputs desired direction

        if current_location == 'Shinganshina District':  # all possible moves from this location
            if user_direction == "East":
                current_location = "Trost District"
                print("You travel east into the Trost District...")
                print("It's not as bad as Shinganshina, but Trost has been left in pretty horrible condition.")
                print("Several titans are still roaming around, I need to be careful, but unlike Shinganshina...")
                print("...there might actually be something useful to find here.\n")
                input()
            elif user_direction == 'Inventory':
                print("You look through your things...")
                print(inventory, '\n')
            elif user_direction == "Exit":
                print("Are you sure? All progress will be lost.")
                print("(Type 'Y' to confirm exit)\n")
                are_you_sure = input()
                if are_you_sure == "Y":
                    print("Simulation exited.")
                    user_decision = "Exit"
                else:
                    user_direction = ''
            elif user_direction == "Scavenge":
                print("There's nothing left to find here.\n")
            else:
                print("Invalid entry.")

        elif current_location == 'Trost District':  # all possible moves from this location
            if user_direction == "North":
                current_location = "Utopia District"
                print("You travel north into the Utopia District...")
            elif user_direction == "South":
                current_location = "Karanes District"
                print("You travel south into the Karanes district...")
            elif user_direction == "East":
                current_location = "Orvud District"
                print("You travel east into the Orvud district...")
            elif user_direction == "West":
                print("There is nothing for you there...\n")
            elif user_direction == 'Inventory':
                print("You look through your things...")
                print(inventory, '\n')
            elif user_direction == "Scavenge":
                if trost_scavenge == 0:
                    print("So many destroyed buildings...")
                    print("So many dead bodies...")
                    print("There are quite a few titans around, but I should be able to search around safely.")
                    input()
                    print("You look around carefully for something to loot...")
                    print("You see the corpse of a Survey corps member, they could have valuable gear...")
                    print("You frantically search the corpse, and find they still have their maneuver gear attached.")
                    input()
                    print("This will be useful for quickly evading titans.\n")
                    print("You have collected: 'Maneuver Gear'")
                    input()
                    maneuver_gear = 'Y'
                    inventory.append("Maneuver Gear")
                    trost_scavenge = trost_scavenge + 1
                else:
                    print("There is nothing left here.\n")
            elif user_direction == "Exit":
                print("Are you sure? All progress will be lost.")
                print("(Type 'Y' to confirm exit)\n")
                are_you_sure = input()
                if are_you_sure == "Y":
                    print("Game exited.")
                    user_decision = "Exit"
                else:
                    user_direction = ''
            else:
                print("Invalid entry.")

        elif current_location == 'Utopia District':  # all possible moves from this location
            if user_direction == "East":
                current_location = "Stohess District"
                print("You travel east into the Stohess District...")
                print("Current location:", current_location, '\n')
            elif user_direction == "South":
                current_location = "Trost District"
                print("You travel south into the Trost district...")
                print("Current location:", current_location, '\n')
            elif user_direction == 'Inventory':
                print("You look through your things...")
                print(inventory, '\n')
            elif user_direction == "Scavenge":
                if utopia_scavenge == 0:
                    print("Something's definitely been through here...")
                    print("but whatever it was... it isn't here now.")
                    input()
                    print("There isn't much left of anything here.")
                    print("No corpses, no titans, just rubble.")
                    input()
                    print("My surroundings are telling me that I'm as safe as ever...")
                    print("but this is the most uncomfortable I've felt yet.\n")
                    print("I really just want to get out of here. What should I do?")
                    print("1: Search through the rubble\n2: Run back to Trost\n")
                    user_choice2 = input()
                    if user_choice2 == '1':
                        print("Ok. Let's hurry up and find something before I leave.\n")
                        print("You run to the nearest pile of rubble and start digging frantically.")
                        print("You uncover a business sign which reads 'Levi's Firearms'")
                        print("Is this the rubble of a gun shop?\n")
                        print("You keep digging...\n")
                        input()
                        print("You found something! An old rifle!!! It has 5 bullets.\n")
                        print("You have collected: 'Rifle'")
                        input()
                        rifle = 'Y'
                        inventory.append("Rifle")
                        utopia_scavenge = utopia_scavenge + 1
                    elif user_choice2 == '2':
                        print("You sprint back to Trost as fast as possible.")
                        print("If there's something I need to find there's no way it's in this empty wasteland.")
                        input()
                        print("You keep running, as fast as possible. Then you see something in the corner of your eye.")
                        input()
                        print("Your body completely freezes.")
                        input()
                        print("You look around frantically...")
                        print("but you don't see anything!")
                        input()
                        print("Oh well, better start running agai-\n")
                        input()
                        print("Before you can even finish the thought, your body is crushed from a hand at least 5 meters long")
                        print("Your last sight is a titan crushing your ribcage...")
                        print("and then everything fades to black.\n")
                        print("SIMULATION FAILED\n")
                        print("Try again? ('Y' for yes, any other entry will exit.)")
                        are_you_sure = input()
                        if are_you_sure == 'Y' or '\n':
                            print("\nReverted to last checkpoint.\n")
                            current_location = 'Utopia District'
                        else:
                            print("Simulation exited.")
                            user_decision = 'Exit'
                    else:
                        print("Invalid entry.")
                        print("\nReverted to last checkpoint.\n")
                        current_location = 'Utopia District'
                else:
                    print("There's nothing left to find here.\n")
            elif user_direction == "Exit":
                print("Are you sure? All progress will be lost.")
                print("(Type 'Y' to confirm exit)\n")
                are_you_sure = input()
                if are_you_sure == "Y":
                    print("Game exited.")
                    user_decision = "Exit"
                else:
                    user_direction = ''
            else:
                print("Invalid entry.")

        elif current_location == 'Karanes District':  # all possible moves from this location
            if user_direction == "East":
                current_location = "Yarckel District"
                print("You travel east into the Yarckel District...")
                print("Current location:", current_location, '\n')
            elif user_direction == "North":
                current_location = "Trost District"
                print("You travel north into the Trost district...")
                print("Current location:", current_location, '\n')
            elif user_direction == 'Inventory':
                print("You look through your things...")
                print(inventory, '\n')
            elif user_direction == "Scavenge":
                if karanes_scavenge == 0:
                    print("There are titans everywhere...")
                    print("but the buildings seem fine, and there are no dead bodies in sight...")
                    print("what's going on here?")
                    input()
                    print("You survey the area to see if anything stands out, "
                          "and then you see a flare gun on the roof of a nearby building!\n")
                    print("How should I get it down?"
                          "I could go inside and try to find an entryway to the roof, "
                          "or I could throw some rubble at it and try to knock it down.")
                    print("1: Go inside\n2: Throw rubble")
                    user_choice3 = input()
                    if user_choice3 == '1':
                        print("Ok. Let's head inside...\n")
                        print("You sneak to the side of the building and try to open the door...")
                        input()
                        print("It's unlocked!!!")
                        input()
                        print("You walk into the room, and are greeted by a humanoid figure standing by the window.")
                        print("You look at the figure and notice a ladder just past them, it should lead to the roof.")
                        input()
                        print("You have no choice but to sneak past them...")
                        input()
                        print("You attempt to sneak past...")
                        print("but the figure lunges toward you!")
                        input()
                        print("Or, at least it seemed that way.")
                        print("Turns out it was just a dead corpse.")
                        input()
                        print("You continue up the ladder and find the flare gun.")
                        print("You have collected: 'Flare gun'")
                        flare_gun = 'Y'
                        inventory.append("Flare gun")
                        karanes_scavenge = karanes_scavenge + 1
                    elif user_choice3 == '2':
                        print("In an area swarming with titans...")
                        print("you stupidly choose to throw a rock at the top of a building.")
                        input()
                        print("You miss the flare gun horribly, and hit a titan in the face.")
                        input()
                        print("A pack of titans races towards you and devours you limb from limb.")
                        input()
                        print("Pitiful.\n")
                        print("SIMULATION FAILED\n")
                        print("Try again? ('Y' for yes, any other entry will exit.)")
                        are_you_sure = input()
                        if are_you_sure == 'Y' or '\n':
                            print("\nReverted to last checkpoint.\n")
                            current_location = 'Karanes District'
                        else:
                            print("Simulation exited.")
                            user_decision = 'Exit'
                    else:
                        print("Invalid entry.")
                        print("\nReverted to last checkpoint.\n")
                        current_location = 'Karanes District'
                else:
                    print("There's nothing left to find here.\n")
            elif user_direction == "Exit":
                print("Are you sure? All progress will be lost.")
                print("(Type 'Y' to confirm exit)\n")
                are_you_sure = input()
                if are_you_sure == "Y":
                    print("Game exited.")
                    user_decision = "Exit"
                else:
                    user_direction = ''
            else:
                print("Invalid entry.")

        elif current_location == 'Yarckel District':  # all possible moves from this location
            if user_direction == "West":
                current_location = "Karanes District"
                print("You travel west into the Karanes District...")
                print("Current location:", current_location, '\n')
            elif user_direction == 'Inventory':
                print("You look through your things...")
                print(inventory, '\n')
            elif user_direction == "Scavenge":
                if yarckel_scavenge == 0:
                    print("You begin looking around a messy, secluded, alley... it reeks.\n")
                    print("You continue to look around...")
                    input()
                    print("You turn the corner and walk straight into a smaller titan, roughly 10ft tall.")
                    print("Luckily for you, its legs and arms have been cut off, and there's a sword dug deep...")
                    print("into its left eye.\n")
                    print("Who in the world could have done this?")
                    input()
                    print("The sword is pretty beat up, but it wouldn't make any sense to leave it.")
                    print("You rip the sword out of the titans eye socket.")
                    print("Item collected: 'Left handed sword'")
                    l_sword = 'Y'
                    inventory.append("Left handed sword")
                    yarckel_scavenge = yarckel_scavenge + 1
                else:
                    print("There's nothing left to find here.\n")
            elif user_direction == "Exit":
                print("Are you sure? All progress will be lost.")
                print("(Type 'Y' to confirm exit)\n")
                are_you_sure = input()
                if are_you_sure == "Y":
                    print("Game exited.")
                    user_decision = "Exit"
                else:
                    user_direction = ''
            else:
                print("Invalid entry.")

        elif current_location == 'Stohess District':  # all possible moves from this location
            if user_direction == "West":
                current_location = "Utopia District"
                print("You travel west into the Utopia District...")
                print("Current location:", current_location, '\n')
            elif user_direction == 'Inventory':
                print("You look through your things...")
                print(inventory, '\n')
            elif user_direction == "Scavenge":
                if stohess_scavenge == 0:
                    print("This area is a polar opposite to the area you just came.")
                    print("You hear screams from every direction...")
                    print("buildings are being destroyed all around you.")
                    input()
                    print("There aren't many titans, but the ones that are here, are much larger than any you've seen before.\n")
                    print("Luckily, this means navigating should be much easier,")
                    print("As the smaller titans are much harder to sneak past.")
                    input()
                    print("You begin to scavenge the area...")
                    input()
                    print("You look for awhile, but can't seem to find anything...")
                    print("Then you see it, a shiny sword, poking out of some rubble.")
                    input()
                    print("You run to grab it, when you hear extremely heavy footsteps marching towards you.")
                    print("Without a second thought you dive to the ground, and look behind you.")
                    print("You look up to a massive titan, at least 50 meters tall, staring over you.")
                    input()
                    print("He steps towards you...")
                    input()
                    print("That's when a loud screech is let out from a building not too far off... it sounds like a kid.")
                    print("The titan marches off towards the building... there's nothing you can do against any titan...")
                    print("let alone a titan that size.")
                    input()
                    print("You pick up the sword and get somewhere safe.")
                    print("Item collected: 'Right handed sword'")
                    r_sword = 'Y'
                    inventory.append("Right handed sword")
                    stohess_scavenge = stohess_scavenge + 1
                else:
                    print("There's nothing left to find here.\n")
            elif user_direction == "Exit":
                print("Are you sure? All progress will be lost.")
                print("(Type 'Y' to confirm exit)\n")
                are_you_sure = input()
                if are_you_sure == "Y":
                    print("Game exited.")
                    user_decision = "Exit"
                else:
                    user_direction = ''
            else:
                print("Invalid entry.")

        elif current_location == 'Orvud District':  # all possible moves from this location
            if user_direction == "West":
                current_location = "Trost District"
                print("You travel east into the Trost District...")
                print("Current location:", current_location, '\n')
            elif user_direction == "North":
                current_location = "Mitras"
                print("WARNING: THIS IS THE FINAL AREA, PLEASE ENSURE YOU ARE READY.")
                print("IF YOU WOULD LIKE TO CONTINUE EXPLORING THE MAP, TRAVEL BACK...")
                print("TO THE ORVUD DISTRICT BEFORE SCAVENGING MITRAS.\n")
                print("SCAVENGING MITRAS WILL ENTER THE FINAL SEQUENCE OF THE GAME.\n")
                print("You travel north into Mitras...\n")
            elif user_direction == 'Inventory':
                print("You look through your things...")
                print(inventory, '\n')
            elif user_direction == "Scavenge":
                if orvud_scavenge == 0:
                    print("Oh my god...")
                    input()
                    print("Wha- how could this have happened?")
                    input()
                    print("This place... it looks even worse than Shinganshina...")
                    input()
                    print("Mysterious man: Hey! Come here!!!\n")
                    print("You look towards the old man, he's trapped under some heavy debris, there's no saving him...")
                    input()
                    print("Mysterious man: Well!? Don't just stand there! Come here!\n")
                    print("You head towards the old man before his screaming draws the attention of any nearby titans.")
                    input()
                    print("Mysterious man: Listen... kid...")
                    print("                you have to get to the capital, Mitras")
                    input()
                    print("You: Yes, I know, it's the only safe place left.")
                    input()
                    print("Mysterious man: Heh, now I wouldn't say that kid...")
                    print("                that's where I just came from.")
                    input()
                    print("You: Why in the hell would you leave Mitras old man!?")
                    print("     Are you crazy!?")
                    input()
                    print("Mysterious man: Heh heh, well perhaps a little, but I guess I didn't have much choice.")
                    print("                You see, Mitras, is no longer the safe haven you know it as.")
                    input()
                    print("(He coughs and spits up blood)\n")
                    print("Mysterious man: Listen kid, do not head to Mitras unless you are completely prepared.")
                    print("                Please just be safe, and take this, I don't need it anymore...")
                    input()
                    print("(The old man dies with his arm extended, holding something in his hand)")
                    input()
                    print("You take what appears to be a syringe with some mysterious fluid inside.")
                    print("Item collected: 'Titan injection'")
                    titan_injection = 'Y'
                    inventory.append("Titan injection")
                    orvud_scavenge = orvud_scavenge + 1
            elif user_direction == "Exit":
                print("Are you sure? All progress will be lost.")
                print("(Type 'Y' to confirm exit)\n")
                are_you_sure = input()
                if are_you_sure == "Y":
                    print("Game exited.")
                    user_decision = "Exit"
                else:
                    user_direction = ''
            else:
                print("Invalid entry.")

        elif current_location == 'Mitras':  # all possible moves from this location
            if user_direction == 'Inventory':
                print("You look through your things...")
                print(inventory, '\n')
            elif user_direction == 'Scavenge':
                print("You enter the island's capital, Mitras, and it's safe to say that it's just as bad as...")
                print("the old man said.")
                input()
                print("Everything is destroyed...")
                input()
                print("There are corpses everywhere...")
                input()
                print("The smell is gut-wrenching...")
                input()
                print("How did the titans get all the way into the capital?")
                print("This place was supposed to be impenetrable.")
                input()
                print("Come to think of it, where are the titans that caused this?")
                input()
                print("The damage is horrendous, but there isn't a titan in sight...")
                input()
                print("Wait...")
                input()
                print("What.")
                input()
                print("Is.")
                input()
                print("That.")
                input()
                print("As you look off into the distance, you can finally see your end destination...")
                print("the capital building.")
                input()
                print("But, that's not all...")
                print("On top of that building is without a doubt, The Armored Titan.")
                input()
                print("It isn't the tallest titan (15 meters) but it's definitely the toughest...")
                print("It'd take a small army just to take out that single titan.")
                print("What in the hell am I supposed to do here?")
                input()
                print("Mysterious soldier: Hey. You.")
                input()
                print("You turn around quickly, and face the soldier, whose standing up on a rooftop.")
                input()
                print("Mysterious soldier: Hey, random civilian standing out in the open...")
                print("                    get up here unless you like being eaten.")
                input()
                print("I don't see any better options, might as well join him.")
                print("You: Yeah, on my way up.")
                input()
                print("You make your way up to the roof where your greeted by the soldier from before, and two others.")
                input()
                print("Mysterious soldier: I'm Levi, these are my subordinates, Mikasa, and Jean")
                print("Levi: We need a way to take down that titan, now do you have something to offer...")
                print("     or should I kick you off the side of this roof right now?")
                input()
                print("Jean: Levi stop, don't worry, we aren't killing you. But we definitely need help if we want...")
                print("to take that thing down. So do you have anything for us?")
                input()
                print("You: I've gathered a few things")
                print(inventory)
                input()
                if len(inventory) == 6:
                    print("Levi: Not bad random civilian, not bad.")
                    input()
                    print("Jean: Not bad!? With all of this we can take this thing down for good.")
                    input()
                    print("Mikasa: Wait... where were you carrying all of that stuff?")
                    input()
                    print("You: Umm...")
                    input()
                    print("Levi: Enough!!! Right now we need to focus on that titan!")
                    print("Jean! Take the rifle, your our best shot. Aim for the eyes, anywhere else won't do much.\n")
                    print("Jean: Yes sir!")
                    print("Jean: Only 5 shots... I better hit them.")
                    input()
                    print("Levi: Let's see, we already have maneuver gear, and swords... Jean has the rifle...")
                    print("      Mikasa take the flare gun!")
                    input()
                    print("Mikasa: Ok!")
                    input()
                    print("Levi: So all that's left is...")
                    print("where... did you get this...")
                    print("(He shoves the syringe towards you)")
                    input()
                    print("You: I don't even know what that is! An old man gave it to me back in Orvud!")
                    input()
                    print("Levi stares at you intensely")
                    input()
                    print("Ok, since you let us dig through all of your stuff, I guess I'll take your word for it.")
                    print("But I don't trust you, so Jean will hold onto it.")
                    input()
                    print("He tosses the syringe to Jean.")
                    print("Levi: By the way, that injection is to turn a human into a titan.")
                    input()
                    print("Levi: Jean! Aim for his eyes.")
                    print("Jean: Eyes are in sight sir!")
                    print("Levi: Mikasa! Shoot the flare.")
                    print("Mikasa shoots the flare, and the armored titan immediately turns towards the four of you.")
                    print("Levi: Jean!")
                    print("Jean: Got it.")
                    input()
                    print("Jean lets off two shots, hits both eyes, and the armored titan immediately screams in pain.")
                    print("Almost immediately after the titan's scream, reinforcements begin to appear...")
                    print("atop all of the buildings surrounding the capital.")
                    input()
                    print("Reinforcement Soldier: Now's our chance!!!")
                    print("Levi: NO, NOT YET!!!")
                    input()
                    print("About half of the reinforcements swarm the titan using maneuver gear and swords to attack.")
                    print("The armored titan crushes all of those who swarmed in one swing.")
                    print("He picks up a handful of corpses and tosses it back at the other reinforcements still on the building.")
                    print("Of the reinforcements that first appeared, only a few remain")
                    input()
                    print("Levi: Do you see his armor you idiots!? We need to break it before we can take him down.")
                    print("Reinforcement Soldier: Captain Levi! We're ready and armed with spike cannons...")
                    print("just say the word.")
                    input()
                    print("Levi: NOW IDIOTS!!! AIM FOR THE BACK OF NECK!!!")
                    input()
                    print("The reinforcements fire off their first shot...")
                    print("It's a hit! Right in the back of the neck!")
                    print("Mikasa: The armor around his neck is gone! Now is our chance!")
                    input()
                    print("Reinforcement Soldier: Firing second round!!!")
                    input()
                    print("Just as the reinforcements fire the second shot, the armored titan charges the building...")
                    print("It destroys the building, and kills the remaining reinforcements, but not before...")
                    print("taking one last shot to the ankle.")
                    input()
                    print("Levi: Mikasa! Let's go!")
                    print("While the titan is picking itself up from the rubble, Levi and Mikasa move in.")
                    print("Mikasa swings in and goes straight for the neck, but the armored titan is ready...")
                    print("He reaches out and bites off her leg while she's swinging through the air.")
                    input()
                    print("Mikasa: AHHHHH!!!")
                    print("Levi: MIKASA!!!")
                    print("Her body falls to ground.")
                    input()
                    print("Levi: AGHHHHHHH!!!!!")
                    print("Levi whips around the armored titan's ankle and cuts it in half.")
                    input()
                    print("However, the armored titan stomped down on Levi's left arm and leg...")
                    print("Leaving him completely helpless.")
                    input()
                    print("The titan begins to reach down towards Levi...")
                    input()
                    print("Jean: Hey! Over here, dummy!")
                    print("The titan turns towards you and Jean")
                    print("Jean: I still got 3 shots left...")
                    input()
                    print("Jean lets off two more shots, hitting the titan in both eyes.")
                    print("Enraged, the titan picks up a huge piece of rubble and tosses it towards you and Jean")
                    input()
                    print("The building collapses with you and Jean on it, and you both fall to the ground...")
                    input()
                    print("...")
                    input()
                    print("Oh god, I was just knocked out. Where's the titan!?")
                    print("You quickly glance up, to see the titan limping in your direction... he's almost done...")
                    print("but so are you...")
                    input()
                    print("You look at the ground and you see the gun within reach and the injection about 20ft further")
                    print("You quickly grab the gun, and fire the last bullet.")
                    input()
                    print("You hit him perfectly in the eye!")
                    print("Please be dead. Please be dead!!!")
                    input()
                    print("The titan collapses to the ground...")
                    print("but he's not dead yet.")
                    input()
                    print("Your only hope is that injection.")
                    input()
                    print("You and the titan both crawl towards each other...")
                    input()
                    print("The titan is getting closer...")
                    input()
                    print("It's not looking good...")
                    input()
                    print("Just as the titan gets within arms reach of the injection, Jean come running out of the debris")
                    print("He sprints full speed towards the injection, but as soon as he grabs it,")
                    print("the titan grabs hold of Jean, and crushes him.")
                    input()
                    print("The injection rolls out of Jean's hand, across the ground, and into your possession.")
                    input()
                    print("Without a second thought, you inject yourself.")
                    print("As the injured titan crawls towards you, you let out a violent scream...")
                    print("and transform into a titan...")
                    input()
                    print("...")
                    input()
                    print("...\n")
                    print("Mysterious Voice: Hey, "
                          "wake up, "
                          "you did it.")
                    input()
                    print("SIMULATION PASSED.")
                    print("CONGRATULATIONS!!!")
                    print("YOU HAVE COMPLETED SIMULATION TRAINING FOR 'TITAN ATTACK'")
                    print("THANKS FOR PARTICIPATING!!!")
                    user_decision = 'Exit'
                else:
                    print("Armored Titan: Yeah that's not enough fam.\n")
                    print("The armored titan crushes all of you and destroys Mitras.\n")
                    print("SIMULATION FAILED\n")
                    print("Try again? ('Y' for yes, any other entry will exit.)")
                    are_you_sure = input()
                    if are_you_sure == 'Y' or '\n':
                        print("\nReverted to last checkpoint.\n")
                        current_location = 'Mitras'
                    else:
                        print("Simulation exited.")
                        user_decision = 'Exit'
            elif user_direction == 'South':
                print("You travel south into the Orvud District...")
                current_location = 'Orvud District'
            elif user_direction == "Exit":
                print("Are you sure? All progress will be lost.")
                print("(Type 'Y' to confirm exit)\n")
                are_you_sure = input()
                if are_you_sure == "Y":
                    print("Game exited.")
                    user_decision = "Exit"
                else:
                    user_direction = ''
            else:
                print("Invalid entry.")


main()








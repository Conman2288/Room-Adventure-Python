
#############################################################
# author: Connor Heard and Emilio El-Zahr
# date: 1 / 06 / 2023
# desc: Pi Activity 1 - Room Adventure
#############################################################
from time import sleep

class Room:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exit_locations = []
        #  Can make an item class
        self.items = []
        self.item_descriptions = []
        self.grabbables = []
        self.grabbables_descriptions = []

    ###########################################
    #Accessors and Mutators
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exit_locations(self):
        return self._exit_locations

    @exit_locations.setter
    def exit_locations(self, value):
        self._exit_locations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def item_descriptions(self):
        return self._item_descriptions

    @item_descriptions.setter
    def item_descriptions(self, value):
        self._item_descriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def grabbables_descriptions(self):
        return self._grabbables_descriptions

    @grabbables_descriptions.setter
    def grabbables_descriptions(self, value):
        self._grabbables_descriptions = value


    # adds an exit to the room
    # exit is a string
    # room is an instance of a Room
    def add_exit(self, exit, room):
      self.exits.append(exit)
      self.exit_locations.append(room)

    # adds an item to the room
    # item is a string
    # desc is a string which describes the item
    def add_item(self, item, desc):
        self.items.append(item)
        self.item_descriptions.append(desc)

    def delete_item(self, item):
        for i in range (len(self.items)):
            if (item == self.items[i]):
                self.item_descriptions.remove(self.item_descriptions[i])
        self.items.remove(item)

   # Changes description of item once an action has been done to it
    def change_description(self, item, new_desc):
        for i in range(len(self.items)):
            if (self.items[i] == item):
                self.item_descriptions[i] = new_desc

    # add a grabbable item to the room
    def add_grabbable(self, item, desc):
        self.grabbables.append(item)
        self.grabbables_descriptions.append(desc)

    # removes a grabbable item from the room
    # item is a string
    def delete_grabbable(self, grabbable):
        self.grabbables.remove(grabbable)

    # return a string description of the room
    def __str__(self):
        # First room name
        s = "You are in {}.\n".format(self.name)
        # Next, items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        # Last, exits from the room
        s += "Possible exits: "
        for exit in self.exits:
            s += exit + " "
            
        return s
    

def create_rooms():
    global current_room
    global r6

    # create the rooms and give them meaningful names
    r1 = Room("Bedroom")
    r2 = Room("Living Room")
    r3 = Room("Restroom")
    r4 = Room("Office")
    r5 = Room("Kitchen")
    r6 = Room("Bat-Cave")
    
    # create Bed Room
    r1.add_exit("restroom", r3)
    r1.add_exit("livingroom", r2)
    r1.add_exit("office", r4)
    #Items
    r1.add_item("chain", "A rusted, iron chain binds your ankle to a wall behind you. The metal digs into your flesh, causing unbearable pain.")
    r1.add_item("bucket", "A plastic bucket with a broom in it. The broom has a long wooden handle, which could be useful." )
    r1.add_item("rug", "Old and matted, the colors have begun to fade from the cloth.")
    r1.add_item("toolcart", "Looks like some tools he uses to torture his victims. It could contain something useful. If only I could reach it.")
    r1.add_item("trash-bag", "The noxious smell of rotting meat permeates your nostrils. It's tied tightly.")
    r1.add_item("nightstand", "Basic wooden nightstand. An empty picture frame rests on top.")
    r1.add_item("bed", "Queen-sized bed. Probably hasn't been washed in years. The killer rests on it.")
    r1.add_item("jeffrey-dahmer", "God he's ugly! And he reeks! He is knocked out cold and snores loudly.")

    #Grabbables
    r1.add_grabbable("broom", "An old broom. Maybe I can use this for something.")

    # create Living Room
    r2.add_exit("bedroom", r1)
    r2.add_exit("kitchen", r5)
    #Items
    r2.add_item("sofa", "A filthy sofa. No telling what he does on here.")
    r2.add_item("tv", "An outdated television set. It is shut off.")
    r2.add_item("lamp", "A simple lamp. A dirty-sock rests on it.")
    r2.add_item("small-table", "A small table by the couch.")
    r2.add_item("painting", "A painting of an elderly woman sitting in chair. This guy has a weird taste in art.")
    r2.add_item("breaker", "A breaker that's missing a switch.")

    #Grabbables
    r2.add_grabbable("dirty-sock", "A dirty sock.")

    # create Restroom
    r3.add_exit("bedroom", r1)
    #Items
    r3.add_item("toilet", "Suspiciously Clean. A plunger sits next to it.")
    r3.add_item("sink", "A basic white sink. Has a metal-tube on it.")
    r3.add_item("medical-cabinet", "Contains a box of matches.")
    r3.add_item("bathtub", "Full of dirty water. There is a crowbar in there.")
    r3.add_item("waste-bin", "Full of trash. But something glimmers inside! Is that a ring?")
    r3.add_item("mirror", "A dirty mirror.")

    #Grabbables
    r3.add_grabbable("plunger", "It reeks . . .")
    r3.add_grabbable("ring", "It has some strange, unreadable etchings on it.")
    r3.add_grabbable("crowbar", "A basic crowbar. I wonder what this could be used for?")
    r3.add_grabbable("matches", "a beat-up box of matches.")
    r3.add_grabbable("metal-tube", "A sleek metal tube. Looks like some kind of hilt.")

    # create Office
    r4.add_exit("bedroom", r1)
    #Items
    r4.add_item("desk", "A large wooden desk. Probably the nicest thing in this house.")
    r4.add_item("file-cabinet", "A filing cabinet. Contains useless documents.")
    r4.add_item("chair", "A nice leather office chair.")
    r4.add_item("safe", "A steel safe under the desk. It looks like there is a key-lock on it!")
    r4.add_item("chalk-board", "Something is scribbled on it.")
    r4.add_item("briefcase", "Full of legal documents.")
    r4.add_item("bookshelves", "Just a bunch of books.")
    r4.add_item("painting", "A painting of dogs playing poker. It looks loose. Maybe I could pry it down.")
    r4.add_item("marble-bust", "A GLORIUS bust of Julius Caesar. A piece of paper rests under it.")
    r4.add_item("fireplace", "An empty fireplace. Cold and full of ashes.")
    r4.add_item("display-case", "Contains an ornate-axe.")

    #Grabbables  
    r4.add_grabbable("ornate-axe", "A very sharp axe with a hand-crafted handle. A collector's item.")

    # create Kitchen
    r5.add_exit("livingroom", r2)
    r5.add_exit("front-door", None)
    #Items
    r5.add_item("table", "Filthy.")
    r5.add_item("chair", "A basic wooden chair. It has the number \"5\" etched on it.")
    r5.add_item("fridge", "Smells of stale milk. But there is a steak-knife inside.")
    r5.add_item("sink", "Full of dirty dishes. Probably hasn't been cleaned in years.")
    r5.add_item("door-mat", "It says \"Welcome Home\". There is a floor grate under it!")
    r5.add_item("cabinets", "Empty. Except for some chocolate pudding.")
    r5.add_item("toaster", "An old-fashioned metal toaster. A picture sticks out of it.")
    r5.add_item("numpad", "A numpad next to the front door! Looks like I'll need a 4-digit code to get out of here.")
    r5.add_item("oven", "Basic outdated gas oven. Has some baked cookies in it.")
    r5.add_item("counter", "Nothing rests on it.")

    #Grabbables
    r5.add_grabbable("picture", "A picture of the killer's mother. A beastly woman.")
    r5.add_grabbable("steak-knife", "A bloodied steak knife. Could prove quite useful.")
    r5.add_grabbable("milk", "It smells awful.")
    r5.add_grabbable("cookies", "Oreo cookies. I think they are expired.")

    # set room 1 as the current room at beginning of the game
    current_room = r1

# If user interacts with the front door then the death message is displayed.
def death():
    Typewrite("The alarm went off and the killer got you!")

# Function takes input from the user and asks if they want to restart the game.
def game_restart():
    global game_ended
    x = input("Do you want to restart the game? (y/n) ")
    if (x == "y" or x == "Y"):
        Typewrite("Game is restarting . . .")
        game_ended = False
    elif (x == "n" or x == "N"):
        exit()
    else:
        Typewrite("I don't understand. Please enter \"y\" for yes and \"n\" for no.")
        game_restart()
# Function allows for the text to display to user at a slower pace (as if someone were typing).
def Typewrite(string):
    for i in range(len(string)):
        print(string[i], end = '', flush=True)
        if (("." == string[i]) or ("!" == string[i])):
            sleep(0.3)
        else:
            sleep(0.025)
    print("\n")

game_ended = False
game_started = True
# restarts the game is user enters "y" or "Y", 
while(True):
    # Introduction to game
    if(game_started):
        Typewrite("You were walking on your way to school when suddely a man in a van offers you some candy.")
        Typewrite("As you reach out for the candy, the man puts a rag on your face and you pass out . . . . .")
        Typewrite("You wake up to find yourself chained to a wall in a dimly lit bedroom.")
        Typewrite("The man who kidnapped you is sleeping on his bed.")
        Typewrite("Can you escape?")
        game_started = False

    if (game_ended):
       game_restart()

    ######START THE GAME############
    inventory = []
    create_rooms()

# Boolean values to check if an ending has been discovered
    death_by_hammer_ending = False
    escape_ending = False
    Caesar_cipher_ending = False
    LOTR_ending = False
    Star_wars_ending = False
    christmas_ending = False
    batman_ending = False

# A bunch of boolean values to make sure the player does not break the game or do actions out of order.
    chain_broken = False
    toolbox_moved = False
    no_hammer_toolcart = False
    no_chaincutters_toolcart = False
    painting_knocked_down = False
    grate_removed = False
    safe_opened = False
    glasses_on = False
    nightstand_drawer_opened = False
    power_on = False
    look_at_nightstand_once = True
    look_at_bust_once = True
    numpad_sequence = False
    table_destroyed = False
    fireplace_filled = False
    fire_place_lit = False
    trashbag_slit = False
    lightsaber_made = False
    cookies_mixed_milk = False
    cookies_on_counter = False


    #Game Loop (Play forever until the player dies or presses ctrl + c)
    while(True):

        # Makes sure the numpad does not become reactivated without interacting with it.
        numpad_sequence = False
        
        # Checks to make sure if a game ending has initiated
        if(game_ended):
            if(death_by_hammer_ending):
                break
            if(escape_ending):
                break
            if(Caesar_cipher_ending):
                break
            if(LOTR_ending):
                break
            if(Star_wars_ending):
                break
            if(christmas_ending):
                break
            if(batman_ending):
                break
            if(mario_ending):
                break


        status = "{}\nYou are carrying: {}".format(current_room, inventory)

        # if the current room is None, then the player is dead
        if (current_room == None):
            death()
            break

        # display status
        print( "=" * 80)
        print(status)

        # prompt for player input
        # game supports a simple language of <verb> <noun>
        # valid verbs: go, look, take
        # valid nouns depend on the verb
        action = input("What to do? ")
        action = action.lower()

        # set a default response
        response = "I don't understand. If you need assistance type \"help\"."

        # Brings up help prompt if the user types in help.
        if (action == "help"):
            print("=" * 80)
            response = ("The only valid commands are \"go\", \"look\", \"take\", and \"use\".\nExamples include: |use key door| go restroom | take stick | look tree |\nTo quit, press ctrl + c")

        # split the user input into words and store the words in a list
        words = action.split(" ")

        # the only exception input is the "use" command
        if (len(words) == 3):
            if (words[0] == "use"):

                verb = words[0]
                noun1 = words[1]
                noun2 = words[2]

                # default response
                response = "This action cannot be done."

                # checks to make sure item is actually in inventory
                for grabbable in inventory:
                    if (noun1 == grabbable):
                        if(noun1 == "bolt-cutters" and noun2 == "chain" and toolbox_moved):
                            # When the chain is broken, the chain item and bolt-cutters will be removed from the game. Character can now move freely.
                            chain_broken = True
                            current_room.delete_item("chain")
                            inventory.remove("bolt-cutters")
                            response = "The chain is broken. I can now move freely!"

                        # If you use hammer on killer, game ends.
                        if (noun1 == "hammer" and noun2 == "jeffrey-dahmer"):
                            response = "You take your hammer and bash in your kidnapper's skull. Well done. You're not an idiot. Ending 2 / 8 completed."
                            death_by_hammer_ending = True
                            game_ended = True

                        # If you use crowbar on painting, A hole in the wall appears revealing a screwdriver grabbable.
                        if (noun1 == "crowbar" and noun2 == "painting"):
                            painting_knocked_down = True
                            current_room.add_item("hole-in-wall", "Looks like he was stashing a screwdriver behind this painting.")
                            response ="The painting fell! There is a hole with something in it here."
                            current_room.delete_item("painting")
                            inventory.remove("crowbar")
                            current_room.add_grabbable("screwdriver", "A philips-head screwdriver. Should prove to be useful.")

                        # If screwdriver is used on floor grate, then a grate hole appears, and a silver key is revealed.
                        if (noun1 == "screwdriver" and noun2 == "floor-grate"):
                            grate_removed = True
                            response = "That floor grate came right off!"
                            current_room.add_item("grate-hole", "There is a silver-key in here!")
                            current_room.delete_item("floor-grate")
                            inventory.remove("screwdriver")
                            current_room.add_grabbable("silver-key", "A small silver-key! I wonder what this can unlock?")

                        # If silver key is used on safe, the safe opens to reveal a pair of glasses
                        if (noun1 == "silver-key" and noun2 == "safe"):
                            safe_opened = True
                            response = "The safe is now open. I wonder what is inside?"
                            current_room.add_grabbable("glasses", "A pair of glasses? Maybe these will reveal hidden things!")
                            inventory.remove("silver-key")
                            current_room.change_description("safe", "Contains a pair of glasses.")

                        # If the picture is used on the empty frame, then a drawer opens on nightstand revealing a breaker switch.
                        if (noun1 == "picture" and noun2 == "empty-frame"):
                            nightstand_drawer_opened = True
                            response = "When you place the picture in the frame, a drawer in the nightstand opens!"
                            inventory.remove("picture")
                            current_room.change_description("nightstand", "The nightstand has an open drawer with a breaker-switch in it!")
                            current_room.add_grabbable("breaker-switch", "A switch that belongs to a breaker.")
                            current_room.delete_item("empty-frame")

                        # If breaker switch is used on breaker, then TV description is updated.
                        if (noun1 == "breaker-switch" and noun2 == "breaker"):
                            power_on = True
                            response = "You hear the buzz of electricity. The tv suddenly shuts on!"
                            current_room.change_description("tv", "The tv displays a white and black static.")
                            current_room.delete_item("breaker")
                            inventory.remove("breaker-switch")


                        # If you use broom on the toolbox, you can get the hammer and bolt-cutters.
                        if (noun1 == "broom" and noun2 == "toolcart"):
                            toolbox_moved = True
                            inventory.remove("broom")
                            current_room.change_description("toolcart", "Looks like there is a hammer and some bolt-cutters in here!")
                            response = "Yes! I was able to move the toolcart to me. Now I can inspect it."
                            current_room.add_grabbable("bolt-cutters", "Hmmph, I wonder what I can do with these?")
                            current_room.add_grabbable("hammer", "A metal hammer with a wood handle. Could be useful.")

                        # If ornate axe is used on table, then the table is turned into a bundle of firewood. Firewood is added to room as grabbable.
                        if (noun1 == "ornate-axe" and noun2 == "table"):
                            table_destroyed = True
                            inventory.remove("ornate-axe")
                            current_room.delete_item("table")
                            current_room.add_item("broken-table", "Could be used for fire-wood.")
                            current_room.add_grabbable("fire-wood", "A bundle of wood. Used to start a fire.")
                            response = "The table is now a bundle of wood."
                        
                        # If fire-wood is used on fireplace, then fireplace description is updated.
                        if (noun1 == "fire-wood" and noun2 == "fireplace"):
                            fireplace_filled = True
                            inventory.remove("fire-wood")
                            current_room.change_description("fireplace", "A fireplace with wood.")
                            response = "You place wood in the fireplace, ready to be lit."

                        # If matches is used on fireplace, then fireplace description is updated and matches are removed from inventory.
                        if (noun1 == "matches" and noun2 == "fireplace" and fireplace_filled):
                            fire_place_lit = True
                            inventory.remove("matches")
                            current_room.change_description("fireplace", "A lit fireplace.")
                            response = "A sudden blaze shines forth. The fire is now lit."
                        
                        # If ring is used with a lit fireplace, then the LOTR ending initiates.
                        if (noun1 == "ring" and noun2 == "fireplace" and fire_place_lit):
                            LOTR_ending = True
                            game_ended = True
                            print("          ___")
                            print("         .';:;'.")
                            print("        /_' _' /\") __")
                            print("        ;a/ e= J/-``  '.")
                            print("        \ ~_   (  -'  ( ;_ ,.")
                            print("         L~`'_.    -.  \ ./  )")
                            print("         ,'-' '-._  _;  )'   (")
                            print("       .' .'   _.'`)  \  \(  |")
                            print("      /  (  .-'   __\{`', \  |")
                            print("     / .'  /  _.-'   `  ; /  |")
                            print("    / /    '-._'-,     / / \ (")
                            print(" __/ (_    ,;' .-'    / /  /_'-._")
                            print("`;-`` ~`  ccc.`   __.`,`     \j\L")
                            print("                 .='/|\7")      
                            print("                   ' `")
                            response = "The one ring to rule them all . . . Ending 4 / 8 completed."

                        # If steak knife is used on trashbag, then a crystal is revealed to the user.
                        if (noun1 == "steak-knife" and noun2 == "trash-bag"):
                            trashbag_slit = True
                            inventory.remove("steak-knife")
                            current_room.add_grabbable("crystal", "It shimmers with an ethereal glow . . .")
                            current_room.change_description("trash-bag", "In the pile of humans guts lies a crystal!")
                            response = "Flesh and human body parts flood out. But something shiny is left in the bag."

                        # If the crystal is used with the metal tube, then a lightsaber is added to the user's inventory.
                        if ((noun1 == "crystal" and noun2 == "metal-tube") or (noun1 == "metal-tube" and noun2 == "crystal")):
                            inventory.remove("metal-tube")
                            inventory.remove("crystal")
                            inventory.append("lightsaber")
                            lightsaber_made = True
                            response = "A laser blade of death appears before your very eyes."

                        # If the lightsaber is made, and the lightsaber is used on killer, then the star wars ending initiates.
                        if (noun1 == "lightsaber" and noun2 == "jeffrey-dahmer" and lightsaber_made):
                            Star_wars_ending = True
                            game_ended = True
                            print("                    8888888888  888    88888")
                            print("                   88     88   88 88   88  88")
                            print("                    8888  88  88   88  88888")
                            print("                       88 88 888888888 88   88")
                            print("                88888888  88 88     88 88    888888")
                            print("")
                            print("                88  88  88   888    88888    888888")
                            print("                88  88  88  88 88   88  88  88")
                            print("                88 8888 88 88   88  88888    8888")
                            print("                 888  888 888888888 88   88     88")
                            print("                  88  88  88     88 88    8888888")
                            print("")
                            response = "I have the high ground . . . Ending 5 / 8 completed."
                        
                        # If milk is used with cookies, then milk-n-cookies is added to inventory
                        if ((noun1 == "milk" and noun2 == "cookies") or (noun1 == "cookies" and noun2 == "milk")):
                            inventory.remove("milk")
                            inventory.remove("cookies")
                            inventory.append("milk-n-cookies")
                            response = "What is this abomination you've made?"
                            cookies_mixed_milk = True

                        # If milk-n-cookies is used on counter then counter's description is updated.
                        if ((noun1 == "milk-n-cookies" and noun2 == "counter" and cookies_mixed_milk)):
                            inventory.remove("milk-n-cookies")
                            current_room.change_description("counter", "Empty, except for a glass of milk and cookies.")
                            cookies_on_counter = True
                            response = "You place the cookies and milk on the counter."

                        # If dirty sock is used on lit fireplace and milk-n-cookies is used on counter, then santa ending initiates.
                        if (noun1 == "dirty-sock" and noun2 == "fireplace" and fire_place_lit and cookies_on_counter):
                            game_ended = True
                            christmas_ending = True
                            print("   *        *        *        __o    *       *")
                            print("*      *       *        *    /_| _     *")
                            print("   K  *     K      *        O'_)/ \  *    *")
                            print("  <')____  <')____    __*   V   \  ) __  *")
                            print("   \ ___ )--\ ___ )--( (    (___|__)/ /*     *")
                            print(" *  |   |    |   |  * \ \____| |___/ /  *")
                            print("    |*  |    |   |     \____________/       *")
                            response = "It was the night before Christmas . . . Ending 6 / 8 completed."

                        # If plunger is used on killer, then Mario ending initiates.
                        if (noun1 == "plunger" and noun2 == "jeffrey-dahmer"):
                            game_ended = True
                            mario_ending = True
                            response = "It's a meeeee! Mario! Ending 8 / 8 complete."


                        break


        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]

            # the verb is: go
            if (verb == "go"):
                response = "I can only look around this room until I get this chain off me."
                if (chain_broken):
                    # default response
                    response = "Invalid exit"

                    # if bat cave is unlocked, then the ending initiates when user go to bat cave.
                    if (noun == "bat-cave"):
                        game_ended = True
                        batman_ending = True
                        print("       _,    _   _    ,_")
                        print("  .o888P     Y8o8Y     Y888o.")
                        print(" d88888      88888      88888b")
                        print("d888888b_  _d88888b_  _d888888b")
                        print("8888888888888888888888888888888")
                        print("8888888888888888888888888888888")
                        print("YJGS8P8Y888P8Y888P8Y888P9Y8888P")
                        print(" Y888   '8'   Y8P   '8'   888Y")
                        print("  '8o          V          o8'")
                        print("    `                     `")
                        Typewrite("Some men just want to watch the world burn . . . Ending 7 / 8 completed.")
                        break

                    # check for valid exits in the current room
                    for i in range (len(current_room.exits)):
                        # a valid exit is found
                        if (noun == current_room.exits[i]):
                            # change current room to the one associated with
                            # specified exit
                            current_room = current_room.exit_locations[i]

                            # set the response (success)
                            response = "Room changed."

                            # no need to check any more exits
                            break

            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."

                # check for valid items in the current room
                for i in range (len(current_room.items)):
                    #a valid item is found
                    if (noun == current_room.items[i]):
                        # set the response to the item's description
                        response = current_room.item_descriptions[i]

                        # Response if toolcart is empty
                        if (noun == "toolcart" and no_chaincutters_toolcart and no_hammer_toolcart):
                            response = "Empty."

                        # Adds the newly discovered grate to the room
                        if (noun == "door-mat"):
                            current_room.add_item("floor-grate", "A metal floor grate that is screwed tightly shut. Something glimmers under it . . .")
                            current_room.delete_item("door-mat")

                        # If glasses on is true and painting in living room is looked at, then description is changed.
                        if (noun == "painting" and glasses_on):
                            response = "The old lady in the painting holding up \"7\" fingers."

                        # If glasses on is true and chalk board is looked at, then description is changed.
                        if (noun == "chalk-board" and glasses_on):
                            response = "A large, red \"2\" can be seen on the board."
                        
                        # If glasses on is true and user looks at mirror in restroom, a number appears
                        if (noun == "mirror" and glasses_on):
                            response = "The mirror is fogged up. You watch a ghostly finger trace out the number \"4\"."
                        
                        # Adds an empty picture frame to bedroom items when nightstand is viewed.
                        if (noun == "nightstand" and look_at_nightstand_once):
                            current_room.add_item("empty-frame", "An empty picture frame.")
                            look_at_nightstand_once = False
                            
                        # If glasses on and power on the tv will display a number
                        if (noun == "tv" and power_on and glasses_on):
                            response = "The static begins to form into a shape. It appears to be a \"7\"!"

                        # If user looks at numpad it asks the user for input.
                        if (noun == "numpad"):
                            numpad_sequence = True

                        # If user looks at Bust of Caesar, a paper is added to the room.
                        if (noun == "marble-bust" and look_at_bust_once):
                            look_at_bust_once = False
                            current_room.add_item("paper", "Jvvs, fvb ruvd h spaasl hivba jyfwavnyhwof! Ayf aol jvkl upul upul upul lpnoa vu aol kvvy.")

                        # If the user has equipped the glasses and interacts with the file cabinet, then the message will be displayed.
                        if (noun == "file-cabinet" and glasses_on):
                            response = "There is note in here. It reads: Mr. Wayne, I have gone away for vacation. The code to your \"garage\" is 4252. Take care."


                        break

            # the verb is: take
            elif (verb == "take"):
                # default response
                response = "I don't see that item."

                # check for valid grabbable items in the current room
                for i in range(len(current_room.grabbables)):
                    # a valid grabbable is found
                    if (noun == current_room.grabbables[i]):
                        # add the item to player's inventory
                        inventory.append(current_room.grabbables[i])

                        # remove grabbable item from the room
                        current_room.delete_grabbable(current_room.grabbables[i])

                        # set the response (success)
                        response = current_room.grabbables_descriptions[i]

                        # These make sure toolbox description is updated when an item is removed
                        if (toolbox_moved and noun == "bolt-cutters"):
                            current_room.change_description("toolcart", "Contains a hammer.")
                            no_chaincutters_toolcart = True
                            response = "Hmmph, I wonder what I can do with these?"
                        if (toolbox_moved and noun == "hammer"):
                            current_room.change_description("toolcart", "Contains bolt-cutters.")
                            no_hammer_toolcart = True
                            response = "A metal hammer with a wood handle. Could be useful."
                    
                        # If the painting is knocked down, player can grab the screwdriver.
                        if(painting_knocked_down and noun == "screwdriver"):
                            current_room.change_description("hole-in-wall", "Empty.")
                            response = "A philips-head screwdriver. Should prove to be useful."
                        
                        # If the grate has been unscrewed, player can 
                        if(grate_removed and noun == "silver-key"):
                            current_room.change_description("grate-hole", "Empty.")
                            response = "A small silver-key! I wonder what this can unlock?"

                        # Makes glasses on True and deletees glasses from inventory.
                        if(safe_opened and noun == "glasses"):
                            current_room.change_description("safe", "Empty.")
                            glasses_on = True
                            inventory.remove("glasses")
                            response = "You put on the glasses. Hidden things will now reveal themselves to you."

                        # All of the following if statements change the description of items within the room once a grabbale has been taken from them.

                        if (noun == "crowbar"):
                            current_room.change_description("bathtub", "Full of dirty water.")

                        if (noun == "plunger"):
                            current_room.change_description("toilet", "Suspiciously clean.")
                        
                        if (noun == "picture"):
                            current_room.change_description("toaster", "Empty.")
                        
                        if (noun == "breaker-switch"):
                            current_room.change_description("nightstand", "Empty.")
                        
                        if (noun == "matches"):
                            current_room.change_description("medical-cabinet", "Empty.")
                            response = "A box of matches."

                        if (noun == "ornate-axe"):
                            current_room.change_description("display-case", "Empty.")

                        if (noun == "fire-wood" and table_destroyed):
                            current_room.delete_item("broken-table")

                        if (noun == "steak-knife"):
                            current_room.change_description("fridge", "Smells of stale milk. Yuck!")

                        if (noun == "crystal" and trashbag_slit):
                            current_room.delete_item("trash-bag")

                        if (noun == "broom"):
                            current_room.change_description("bucket", "Empty.")
                        
                        if (noun == "ring"):
                            current_room.change_description("waste-bin", "Full of trash.")
                        
                        # no need to check any more grabbable items
                        break
        # display the response
        print("=" * 80)

        Typewrite("\n{}".format(response))
        
        if (numpad_sequence):
            print("-------------------------")
            print("|       |  ABC  |  DEF  |")
            print("|   1   |   2   |   3   |")
            print("-------------------------")
            print("|  GHI  |  JKL  |  MNO  |")
            print("|   4   |   5   |   6   |")
            print("-------------------------")
            print("| PQRS  |  TUV  | WXYZ  |")
            print("|   7   |   8   |   9   |")
            print("-------------------------")
            print("|       |       |       |")
            print("|   *   |   0   |   #   |")
            print("-------------------------")
            numbers = int(input("Enter 4 digits: "))
            if (numbers == 5724):
                game_ended = True
                escape_ending = True
                print("             ,")
                print("        _.-'` `'-.")
                print("       '._ __{}_(")
                print("         |'--.__\ ")
                print("        (   ^_\^")
                print("         |   _ |")
                print("         )\___/")
                print("     .--'`:._]")
                print("    /  \      '-.")
                Typewrite("The door unlocks and you open it to freedom. You alert the neighbors and they call the police. Ending 1 / 8 complete.")
            elif (numbers == 9998):
                game_ended = True
                Caesar_cipher_ending = True
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⢿⡶⠆⠀⠀⠀⢀⡀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠻⠋⣠⠀⢀⣶⠇⢠⣾⡿⠁⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⢀⣼⠟⠋⠻⢁⣴⠀⣾⣿⠀⠾⠟⠀⠈⣉⣠⣦⡤⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠸⠃⣠⡆⠀⣿⡟⠀⠛⠃⠀⠀⣶⣶⣦⣄⠉⢁⡄⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⣰⡀⢰⣿⠇⠀⢉⣀⣀⠛⠿⠿⠦⠀⢀⣠⣤⣴⣾⡇⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⣿⠃⠀⠠⣴⣦⡈⠙⠛⠓⠀⢰⣶⣶⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀")
                print("⠀⠀⢀⣤⠦⡀⠰⢷⣦⠈⠉⠉⠀⣰⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀")
                print("⠀⠀⠈⠁⠀⠘⣶⣤⣄⣀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠃⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣯⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣷⣤⣈⡉⠛⠛⠛⠛⠻⠟⠛⠛⠛⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀")
                Typewrite("E tu, Brute? Ending 3 / 8 complete.")
            elif (numbers == 4252):
                current_room.add_exit("bat-cave", r6)
                Typewrite("The kitchen counter begins to shift, revealing a staircase to somewhere . . .")
            else:
                Typewrite("That is incorrect . . .")
                numpad_sequence = False

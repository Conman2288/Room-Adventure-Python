######################################################################
# Name: Dominic Rosario
# Date: 1/4/2023
# Description: Room Adventure
######################################################################
######################################################################
# the blueprint for a room
class Room:
# the constructor
    def __init__(self, name):    
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
    # getters and setters for the instance variables
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
    def exitLocations(self):
        return self._exitLocations
    
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value
        
    @property
    def items(self):
        
        return self._items
    @items.setter
    def items(self, value):
        self._items = value
        
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value
        
    @property
    def grabbables(self):
        return self._grabbables
    
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value


    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)


    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made
    # of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)
        
    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    def delGrabbable(self, item):
        # append the item to the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)
        
        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + ", "
        
            # next, the exits from the room
        s += "\n"
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        
        return s

######################################################################
# creates the rooms
def createRooms():
    # r1 through r4 are the four rooms in the mansion
    # currentRoom is the room the player is currently in (which can
    # be one of r1 through r4)
    # since it needs to be changed in the main part of the program,
    # it must be global
    global currentRoom
    
    # create the rooms and give them meaningful names
    r1 = Room("The Post Office")
    r2 = Room("The Saloon")
    r3 = Room("The Genral Store")
    r4 = Room("The Stable")
    
    # add exits to room 1
    r1.addExit("east", r2) # -> to the east of room 1 is room 2
    r1.addExit("south", r3)
    
    # add grabbables to room 1
    r1.addGrabbable("revolver")
    
    # add items to room 1
    r1.addItem("wall", "It has tens of empty wooden boxes, likey where mail would end up \nif there was anyone left to mail anything to")
    r1.addItem("desk", "It is made of wood, old and rotted to the point its malluable\nlike putty, your golden revolver is sunk into the center of the desk")
    r1.addItem("room", "Old and dusty, galss is shrewn around from a moment ago when you crashed through the window.")
    
    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    
    # add items to room 2
    r2.addItem("stairs", "It likely heads upstairs to the hotel rooms, but I wouldnt trust\nthose staris as much as i would trust a job to go right")
    r2.addItem("bar", "All the Alcohol is gone, not suprised.")
    
    # add exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    
    # add grabbables to room 3
    r3.addGrabbable("stash")
    
    # add items to room 3
    r3.addItem("bookshelves", "They are some small books left, however id bet they're\nso matted opening one would destroy it")
    r3.addItem("counter", "You see that the window next to the counter is shattered,\ntaking a peak behind it.... ITS THERE! THE STASH!!")
    r3.addItem("medicine_cabnet", "Just about empty, whatever is left is bound to do\nthe opposite of what its supposed to")
    
    # add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("horse?", None) # DEATH!
    
    # add grabbables to room 4
    r4.addGrabbable("saddle")

    # add items to room 4
    r4.addItem("wooden_stable","It looks like the only thing thats lasted the test of time, theres some grass growing.")
    r4.addItem("horse", "Its your horse! he came back for you, his pitch black tone\nstanding as a contrast to the setting sun in the horizon")

    # set room 1 as the current room at the beginning of the game
    currentRoom = r1



# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + "" * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + "" * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")

def win():
    print("                                                                     |\../|")
    print("                                                                     |    |")
    print("                                                                 \.__;    ;__./")
    print("                                             |\    /|             \__________/")
    print("                                          ___| \,,/_/             $$$ ^  o $$$")
    print("                                       ---__/ \/    \              $$//""\\$$")
    print("                                      __--/     (D)  \             $  \\\\  $")
    print("                                      _ -/    (_      \       .--.___/    \___.--.")
    print("                                     // /       \_ / ==\      |  |   \    /   |  ;")
    print("               __-------_____--___--/           / \_ O o)     |  ||~| |  | |~||  |  /---\"")
    print("              /                                 /   \==\\     |  ;|_| |  | |_|:  |/ ._;`|")
    print("             /                                 /        \\    \  ;____|  |____:   ./   |  |")
    print("            ||          )                   \_/\         \\    \.. ||||[]||||__\./    [|  |")
    print("            ||         /              _      /  |         \    // [|   ||        \    [|  |")
    print("            | |      /--______      ___\    /\  :          \  //  [:   ||.____.   |\   |  |")
    print("            | /   __-  - _/   ------    |  |   \ \           \/   /|   |      |   ;\   |  |")
    print("            |   -  -   /                | |     \ )              /|   |      \___/\   |  |")
    print("            |  |   -  |                 | )     | |              /|   |       | :     |  |")
    print("            | |    | |                 | |    | |               /|   |       : --^[[|  |")
    print("            | |    < |                 | |   |_/                 \___/      |__---^[[|  |")
    print("            < |    /__\                <  \                      .| |                |  |")
    print("            /__\                       /___\                    (__))                |  |")
    

######################################################################
# START THE GAME!!!
print("The Old West is a place of almost infinite wealth surrounded by unyielding death.")
print("You and your crew just pulled off your biggest heist yet, robbing 4 high values trains")
print("all at the same time. After reconveining the law is hot on your trail and you flee to a")
print("nearby ghost town. BUT! as you approach the town a rival gang attacks sending you")
print("off your horse. While flying through the air you glimpse the stash of money fly off the")
print("horse as well and go into the town. Crashing into a building you hear your horse run off")
print("and the screams of gang members, lawmen, and your crew slowly drift off into the horizon")
print("FIND THE MONEY, GET OUT OF TOWN!!")
inventory = [] # nothing in inventory...yet
createRooms() # add the rooms to the game

# play forever (well, at least until the player dies or asks to quit)
while (True):
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)
    
    # if the current room is None, then the player is dead
    # this only happens if the player goes south when in room 4
    if (currentRoom == None):
        print("========================================================")
        if ("stash" in inventory):
            print("You have left town on your horse, The stash resting on the back of the\nhorse gleaming off the setting sun, You have Won")
            win()
            break
        else:
            print("You have left town on your horse, leaving behind the stash...Worthless")
            death()
            break
    # display the status
    print("========================================================")
    print(status)
  
    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    action = input("What to do? ")

    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to known values
    action = action.lower()


    # exit the game if the player wants to leave (supports quit,
    # exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break


    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
    # split the user input into words (words are separated by spaces)
    words = action.split()


    # the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if (verb == "go"):
            # set a default response
            response = "Invalid exit."

            # check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if (noun == currentRoom.exits[i]):
                    # change the current room to the one that is
                    # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]

                    # set the response (success)
                    response = "Room changed."
                    # no need to check any more exits
                    break
                
        # the verb is: look
        elif (verb == "look"):
            # set a default response
            response = "I don't see that item."

            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if (noun == currentRoom.items[i]):
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]

                    # no need to check any more items
                    break
                
        # the verb is: take
        elif (verb == "take"):
            # set a default response
            response = "I don't see that item."

            # check for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable):
                    # add the grabbable item to the player's
                    # inventory
                    inventory.append(grabbable)

                    # remove the grabbable item from the room
                    currentRoom.delGrabbable(grabbable)

                    # set the response (success)
                    response = "Item grabbed."

                    # no need to check any more grabbable items
                    break
    # display the response
    print("\n{}".format(response))
            

                    



        

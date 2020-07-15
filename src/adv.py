
import sys
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
player = Player(input("Select a name: "), room["outside"])
print(f"Welcome {player.name}. Your location is: {player.location}")

way = ""
directions = ["north", "east", "west", "south", "quit"]

def main_prompt():
	way = input(f"{player.name}, choose a direction: ")
	while way.lower() not in directions:
		print("Please choose a valid direction.")
		way = input(": ")
	if way.lower() == "quit":
		sys.exit()
	else:
		move_player(way.lower())

def move_player(direction):
    if direction == "north":
        if player.location.n_to is None:
            print("The way is blocked! Choose again!")
        else:
            player.location = player.location.n_to
            print(f"You are now in the: {player.location}")
        
    elif direction == "east":
        if player.location.e_to is None:
            print("The way is blocked! Choose again!")
        else:
            player.location = player.location.e_to
            print(f"You are now in the: {player.location}")
                    
    elif direction == "west":
        if player.location.w_to is None:
            print("The way is blocked! Choose again!")
        else:
            player.location = player.location.w_to
            print(f"You are now in the: {player.location}")
            
    elif direction == "south":
        if player.location.s_to is None:
            print("The way is blocked! Choose again!")
        else:
            player.location = player.location.s_to
            print(f"You are now in the: {player.location}")
    
            
def main_game_loop():
	while True:
	    main_prompt()
  
main_game_loop()






    

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

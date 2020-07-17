import os
import sys
import time
from room import Room
from player import Player
from item import Item


# Declare all the rooms


items = [Item("sword", "a steel sword"), Item("dagger", "a marble dagger"), Item("shield", "a largely useless wood shield"), Item("amelet", "A magical amelet that brings only bad luck to its owner"), Item("cape", "A wool cape that can be used for sleeping or fashion")]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items[0], items[1]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items[1]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items[2]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items[3]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items[4]]),
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


player1 = Player(room["outside"], [])

def clear_screen():
    os.system("cls")

def display_items():
    output = "Room Contents: "
    count = 1
    for k, v in room.items():
        if v == player1.location:
            for i in room[k].inventory:
                output += f"\n {count}: {i}"
                count += 1
            print(f"\n{output}\n")
            
def display_player_items():
    output = "Player Inventory: "
    count = 1
    for item in player1.inventory:
        output += f"\n {count}: {item}"
        count += 1
    print(f"{output}\n")
            
def add_items(name):
    for k, v in room.items():
        if v == player1.location:
            for i in room[k].inventory:
                if i.name == name:
                    player1.inventory.append(i)
                    index = items.index(i)
                    items[index].on_take(i, player1)
            remove_room_item()
            
            
def add_item_room(item):
    for k, v in room.items():
        if v == player1.location:
            room[k].inventory.append(item)
    display_items()
            
def remove_player_item(name, index):
    for item in player1.inventory:
        if name == item.name:
            player1.inventory.remove(item)
            items[index].on_drop(item, player1)          
            
def remove_room_item():
    for k, v in room.items():
        if v == player1.location:
            for i in room[k].inventory:
                room[k].inventory.remove(i)
            display_items()
            
def drop_items(name):
    for item in player1.inventory:
        if name == item.name:
            index = items.index(item)
            remove_player_item(name, index)
            add_item_room(item)
            
def title_screen():
    question1 = "What is your name ?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    player1.name = player_name
    
    clear_screen()
    statement1 = f"Welcome {player1.name}. Your location is: {player1.location}\n"
    for character in statement1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    display_items()
    
title_screen()         

way = ""
directions = ["north", "east", "west", "south", "quit", "inventory"]
command = ["take", "get", "drop"]

def main_prompt():
    way = input(f"{player1.name}, choose a direction, type inventory for a list of player's items or type 'take', 'get' or 'drop' + name of an item inside the room you wish to add or drop \n").lower()
    if len(way.split()) > 1:
        while way.split()[0] not in command:
            print("\nPlease choose a direction, type i or inventory for a list of player's items or type 'take', 'get' or 'drop' + name of an item inside the room you wish to add or drop")
            way = input("> ")
        if way.split()[0] == "drop":
            drop_items(way.split()[1])
        else:
           add_items(way.split()[1]) 
    else:
        while way not in directions:
            print("\nPlease choose a direction or type name of item you wish to add")
            way = input("> ")
        if way == "quit":
            sys.exit()
        elif way == "inventory":
            display_player_items()
        else:
            move_player(way.lower())

def move_player(direction):
    if direction == "north":
        if player1.location.n_to is None:
            print("\nThe way is blocked! Choose again!")
        else:
            clear_screen()
            player1.location = player1.location.n_to
            print(f"\nYou are now in the: {player1.location}")
            display_items()
        
    elif direction == "east":
        if player1.location.e_to is None:
            print("\nThe way is blocked! Choose again!")
        else:
            clear_screen()
            player1.location = player1.location.e_to
            print(f"\nYou are now in the: {player1.location}")
            display_items()
                    
    elif direction == "west":
        if player1.location.w_to is None:
            print("\nThe way is blocked! Choose again!")
        else:
            clear_screen()
            player1.location = player1.location.w_to
            print(f"\nYou are now in the: {player1.location}")
            display_items()
            
    elif direction == "south":
        if player1.location.s_to is None:
            print("\nThe way is blocked! Choose again!")
        else:
            clear_screen()
            player1.location = player1.location.s_to
            print(f"\nYou are now in the: {player1.location}")
            display_items()
            

    
def main_game_loop():
	while True:
	   main_prompt()
  
main_game_loop()


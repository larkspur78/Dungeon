# key
# ------------------------------------------------------------------------------
# 0 Hall        1 Kitchen
# 2 Armory      3 Cellar    4 Treasury

# ---------
# | 0 | 1 |
# -------------
# | 2 | 3 | 4 |
# -------------
import sys


def room_0():
    # description
    description = "Welcome to the Hall in the Dungeon. Your goal is to find the hidden chest of gold in one of the rooms.\n"
    # doors
    number_doors = "There are two doors out of this room. One leads East to the Kitchen. One leads South to the Armory.\n"
    # where those doors go
    doors = {"east": room_1, "south": room_2}
    return process_user_movement(description, number_doors, doors)


def room_1():

    description = "You have found the very small Kitchen. You barely fit here. You're like Alice in that crazy-tiny-room thing.\n"
    number_doors = "There are two doors out of this room. One leads West to the Hall. The other leads South to the Cellar.\n"
    doors = { "south": room_3, "west": room_0}
    return process_user_movement(description, number_doors, doors)
    print("\n")


def room_2():

    description = "You have found the Armory and awoken a very angry two-headed Dragon.\n"
    number_doors = "There are two doors out of this room. One leads North to the Hall. The other leads East to the Cellar.\n"
    doors = {"north": room_0, "east": room_3}
    return process_user_movement(description, number_doors, doors)


def room_3():

    description = "You have found the Cellar. Nothing resides here except diseased bats.\n"
    number_doors = "There are three doors out of this room. One leads North to the Kitchen, one leads West to the Armory, and the other door leads East to the Treasury.\n"
    doors = {"north": room_1, "west": room_2, "east": room_4}
    return process_user_movement(description, number_doors, doors)


def room_4():

    description = "Congratulations! You have found the Treasury. You have also found more gold than you could ever carry.\n"
    number_doors = "It is time to exit the Dungeon and make your way to the nearest tavern for a mug of strong braggot.\n"

    print(description)
    print(number_doors)
    user_input = input("Enter 'X' to exit or 'R' to restart: \n").upper()
    if user_input == "X":
        print('Goodbye.')

    if user_input == "R":
        room_0()

    # Write the process_user_movement that moves a user from room to room until they have found the treasure:

def process_user_movement(description, number_doors, doors):
    """
       This is the process_user_movement function that will
       handle a user's input.

    Args:
        doors: A description of the current room
        description: dictionary with door:location sets
    """
    # Print the description of the current room
    print(description)
    # Print the available doors
    print(number_doors)
    # Prompt the user for what door they want to enter
    choice = input("Type in the direction you wish to exit out of this room: \n").lower()

    # Invalid response: Ask them again
    while choice not in doors:
        print("The valid options are: ", list(doors.keys()))
        choice = input("Type in the direction you wish to exit out of this room: \n").lower()

    # Valid response: Go to the correct location
    if choice in doors:
        new_room = doors[choice]
        new_room()


room_0()

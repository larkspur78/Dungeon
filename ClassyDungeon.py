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

class Rooms:

    def __init__(self, description, number_doors, door_direction):
        self.description = description
        self.number_doors = number_doors
        self.door_direction = door_direction


room_0 = Rooms("Welcome to the Hall in the Dungeon. Your goal is to find the hidden chest of gold in one of the rooms.\n",
              "There are two doors out of this room. One leads East to the Kitchen. One leads South to the Armory.\n",
              {}
              )


room_1 = Rooms("You have found the very small Kitchen. You barely fit here. You're like Alice in that crazy-tiny-room thing.\n",
              "There are two doors out of this room. One leads West to the Hall. The other leads South to the Cellar.\n",
              {}
              )


room_2 = Rooms("You have found the Armory and awoken a very angry two-headed Dragon.\n",
               "There are two doors out of this room. One leads North to the Hall. The other leads East to the Cellar.\n",
               {}
               )


room_3 = Rooms("You have found the Cellar. Nothing resides here except diseased bats.\n",
               "There are three doors out of this room. One leads North to the Kitchen, one leads West to the Armory, and the other door leads East to the Treasury.\n",
               {}
               )


room_4 = Rooms("Congratulations! You have found the Treasury. You have also found more gold than you could ever carry.\n",
               "It is time to exit the Dungeon and make your way to the nearest tavern for a mug of strong braggot.\n",
               {}
               )

room_0.door_direction = {"east": room_1, "south": room_2}
room_1.door_direction = {"south": room_3, "west": room_0}
room_2.door_direction = {"north": room_0, "east": room_3}
room_3.door_direction = {"north": room_1, "west": room_2, "east": room_4}
room_4.door_direction = {"restart":room_0}


def game(room):
    print(room.description)
    print(room.number_doors)

    if "restart" in room.door_direction:
        user_input = input("Enter 'X' to exit or 'R' to restart: ").upper()

        if user_input == 'X':
            print("Goodbye")
            exit()

        if user_input == 'R':
            game(room_0)



    print("The valid options are: ", list(room.door_direction.keys()),"\n")

#choice = input("Type in the direction you wish to exit out of this room: \n").lower()

    choice = input("Type in the direction you wish to exit out of this room: \n").lower()

# Invalid response: Ask them again
    while choice not in room.door_direction:
        print("The valid options are: ", list(room.door_direction.keys()))
        choice = input("Type in the direction you wish to exit out of this room: \n\n").lower()

# Valid response: Go to the correct location

    if choice in room.door_direction:
        new_room = room.door_direction[choice]

        game(new_room)


game(room_0)

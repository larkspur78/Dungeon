def room0():
    # description
    description = "This room is very small. You barely fit here. You're like Alice in that crazy-tiny-room thing."
    # doors
    # where those doors Go
    doors = { "east": room2, "west": room1 }

    return process_user_movement(description, doors)

    # Write the process_user_movement that moves a user from room to room until they have found the exit:

def process_user_movement(description, doors):
    """
       This is the process_user_movement function that will
       handle a user's input.

    Args:
        doors: A description of the current room
        description: dictionary with door:location sets
    """
    # Print the description of the current room

    # Print the available doors

    # Prompt the user for what door they want to enter

        # Valid response: Go to the correct location

        # Invalid response: Ask them again

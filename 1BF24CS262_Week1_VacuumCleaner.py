# Goal-Based Vacuum Cleaner Agent

# Initial state of the rooms
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

# Initial position of vacuum cleaner
position = "A"

# Goal state
goal = {
    "A": "Clean",
    "B": "Clean"
}


# Check whether goal is reached
def goal_reached():
    return rooms == goal


print("Initial State:")
print("Room A:", rooms["A"])
print("Room B:", rooms["B"])
print("Vacuum Position:", position)

print("\nStarting Cleaning...\n")


while not goal_reached():

    # If current room is dirty, clean it
    if rooms[position] == "Dirty":

        print("Position:", position)
        print("Action: CLEAN")

        rooms[position] = "Clean"

    # If current room is clean, move to the other room
    else:

        if position == "A" and rooms["B"] == "Dirty":
            print("Position: A")
            print("Action: TURN RIGHT")
            position = "B"

        elif position == "B" and rooms["A"] == "Dirty":
            print("Position: B")
            print("Action: TURN LEFT")
            position = "A"


print("\nGoal State Reached!")
print("Room A:", rooms["A"])
print("Room B:", rooms["B"])
print("Vacuum Position:", position)
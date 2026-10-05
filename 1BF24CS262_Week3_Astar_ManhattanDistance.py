initial = (2, 8, 3,
           1, 6, 4,
           7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


# Manhattan Distance heuristic
def manhattan(state):
    distance = 0

    for tile in range(1, 9):

        current = state.index(tile)
        target = goal.index(tile)

        current_row = current // 3
        current_col = current % 3

        target_row = target // 3
        target_col = target % 3

        distance += abs(current_row - target_row)
        distance += abs(current_col - target_col)

    return distance


# Generate possible moves
def moves(state):
    result = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            result.append(tuple(new_state))

    return result


# A* Search
open_list = []
closed = []

g = 0
h = manhattan(initial)
f = g + h

open_list.append((f, g, initial, [initial]))

while open_list:

    # Select state with minimum f
    current = min(open_list, key=lambda x: x[0])
    open_list.remove(current)

    f, g, state, path = current

    if state in closed:
        continue

    closed.append(state)

    # Check goal
    if state == goal:

        print("Solution Found!")
        print("Number of moves:", g)
        print()

        for s in path:
            print(s[:3])
            print(s[3:6])
            print(s[6:])
            print()

        break

    # Generate next states
    for next_state in moves(state):

        if next_state not in closed:

            new_g = g + 1
            new_h = manhattan(next_state)
            new_f = new_g + new_h

            open_list.append(
                (new_f, new_g, next_state, path + [next_state])
            )

else:
    print("No solution")
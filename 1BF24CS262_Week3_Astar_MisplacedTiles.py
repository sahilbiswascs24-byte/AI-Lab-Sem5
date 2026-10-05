import heapq

# Initial and goal states
initial = (2, 8, 3,
           1, 6, 4,
           7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


# Calculate number of misplaced tiles
def misplaced_tiles(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


# Generate possible next states
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


# Print puzzle
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# A* Search
def a_star():

    # (f, g, state, path)
    open_list = []

    g = 0
    h = misplaced_tiles(initial)
    f = g + h

    heapq.heappush(open_list, (f, g, initial, [initial]))

    visited = set()

    while open_list:

        f, g, current, path = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            print("Goal reached!")
            print("Number of moves:", g)
            print()

            for state in path:
                print_puzzle(state)

            return

        for next_state in get_neighbors(current):

            if next_state not in visited:

                new_g = g + 1
                new_h = misplaced_tiles(next_state)
                new_f = new_g + new_h

                heapq.heappush(
                    open_list,
                    (new_f, new_g, next_state, path + [next_state])
                )

    print("No solution found.")


# Run A*
a_star()
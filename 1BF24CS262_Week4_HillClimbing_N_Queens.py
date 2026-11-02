from itertools import combinations

N = 4

# Calculate attacking queen pairs
def attacking_pairs(state):
    pairs = []

    for i, j in combinations(range(N), 2):
        same_row = state[i] == state[j]
        same_diagonal = abs(state[i] - state[j]) == abs(i - j)

        if same_row or same_diagonal:
            pairs.append((i, j))

    return pairs


# Calculate cost of a state
def cost(state):
    return len(attacking_pairs(state))


# Display chessboard
def print_board(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print("Q", end="  ")
            else:
                print(".", end="  ")
        print()
    print()


# Hill Climbing Algorithm
def hill_climbing(initial_state):

    current = tuple(initial_state)
    iteration = 1

    while True:

        current_cost = cost(current)

        print("Iteration:", iteration)
        print("Current State:", current)
        print("Current Cost:", current_cost)

        print("\nCurrent Board:")
        print_board(current)

        # Check whether goal is reached
        if current_cost == 0:
            print("Goal State Reached!")
            return current

        neighbors = []

        # Generate all neighbours
        for i, j in combinations(range(N), 2):

            neighbor = list(current)

            neighbor[i], neighbor[j] = (
                neighbor[j], neighbor[i]
            )

            neighbor = tuple(neighbor)
            neighbor_cost = cost(neighbor)

            pairs = attacking_pairs(neighbor)

            print(
                f"Swap (x{i}, x{j}) -> {neighbor}, "
                f"Cost = {neighbor_cost}, "
                f"Attacking pairs = {pairs}"
            )

            neighbors.append(
                (neighbor_cost, i, j, neighbor)
            )

        # Select minimum-cost neighbour.
        # Ties are resolved by smallest column indices.
        best_cost, i, j, best_neighbor = min(
            neighbors,
            key=lambda x: (x[0], x[1], x[2])
        )

        # Stop if no improvement is possible
        if best_cost >= current_cost:
            print("No better neighbour found.")
            return current

        print(f"\nSelected Swap: (x{i}, x{j})")
        print("Next State:", best_neighbor)
        print("-----------------------------\n")

        current = best_neighbor
        iteration += 1


# Initial configuration from Week-4 PPT
initial_state = [3, 1, 2, 0]

solution = hill_climbing(initial_state)

print("\nFinal Solution:", solution)
print("Final Cost:", cost(solution))

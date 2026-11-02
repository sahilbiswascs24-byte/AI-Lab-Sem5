import random
import math

N = 8

# Calculate attacking queen pairs
def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            if state[i] == state[j]:
                conflicts += 1

            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate a random neighbour
def get_neighbor(state):
    neighbor = state.copy()

    col = random.randrange(N)
    new_row = random.randrange(N - 1)

    if new_row >= neighbor[col]:
        new_row += 1

    neighbor[col] = new_row

    return neighbor


# Simulated Annealing Algorithm
def simulated_annealing():

    while True:

        current = [random.randrange(N) for _ in range(N)]

        T = 10.0

        while T > 0.01:

            if cost(current) == 0:
                return current

            next_state = get_neighbor(current)

            delta = cost(current) - cost(next_state)

            if delta > 0:
                current = next_state

            else:
                probability = math.exp(delta / T)

                if random.random() < probability:
                    current = next_state

            T = T * 0.995


# Display chessboard
def print_board(state):
    for row in range(N):
        for col in range(N):

            if state[col] == row:
                print("Q", end=" ")

            else:
                print(".", end=" ")

        print()


# Main program
solution = simulated_annealing()

print("Final Solution:", solution)
print("Cost:", cost(solution))

print("\nChessboard:")
print_board(solution)
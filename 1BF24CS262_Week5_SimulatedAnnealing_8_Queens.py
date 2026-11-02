
import random
import math

N = 8

INITIAL_TEMP = 100.0
MIN_TEMP = 0.01
COOLING_RATE = 0.995
MAX_RESTARTS = 100


def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            if state[i] == state[j]:
                conflicts += 1

            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def get_neighbor(state):
    neighbor = state.copy()

    col = random.randrange(N)
    old_row = neighbor[col]

    new_row = random.randrange(N - 1)

    if new_row >= old_row:
        new_row += 1

    neighbor[col] = new_row

    return neighbor


def print_board(state):
    for row in range(N):
        for col in range(N):

            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


def simulated_annealing():

    for restart in range(1, MAX_RESTARTS + 1):

        current = [random.randrange(N) for _ in range(N)]

        T = INITIAL_TEMP
        iteration = 1

        print("\n========== RESTART", restart, "==========")
        print("Initial State:", current)
        print("Initial Cost:", cost(current))

        while T > MIN_TEMP:

            current_cost = cost(current)

            if current_cost == 0:
                print("\nGOAL STATE REACHED!")
                print("Final State:", current)
                print("Final Cost:", current_cost)
                return current

            previous_state = current.copy()

            neighbor = get_neighbor(current)
            neighbor_cost = cost(neighbor)

            deltaE = neighbor_cost - current_cost

            if deltaE <= 0:
                probability = 1.0
            else:
                probability = math.exp(-deltaE / T)

            random_value = random.random()

            if deltaE <= 0 or random_value < probability:
                current = neighbor.copy()
                status = "ACCEPTED"
            else:
                status = "REJECTED"

            print("\n--------------------------------")
            print("Iteration:", iteration)
            print("Temperature:", round(T, 4))
            print("Current State:", previous_state)
            print("Neighbour State:", neighbor)
            print("Current Cost:", current_cost)
            print("Neighbour Cost:", neighbor_cost)
            print("Delta E =", neighbor_cost, "-", current_cost, "=", deltaE)
            print("Acceptance Probability:", round(probability, 6))
            print("Random Value:", round(random_value, 6))
            print("Decision:", status)
            print("State After Decision:", current)

            T = T * COOLING_RATE

            print("New Temperature:", round(T, 4))

            iteration += 1

            if cost(current) == 0:
                print("\nGOAL STATE REACHED!")
                print("Final State:", current)
                print("Final Cost:", cost(current))
                return current

        print("\nTemperature reached minimum.")
        print("Restarting with a new random configuration.")

    print("\nNo solution found within restart limit.")
    return None


solution = simulated_annealing()

if solution is not None:
    print("\n========== FINAL RESULT ==========")
    print("Board Size:", N, "x", N)
    print("Final Configuration:", solution)
    print("Final Cost:", cost(solution))
    print("\nFinal Chessboard:")
    print_board(solution)
else:
    print("Try increasing MAX_RESTARTS.")

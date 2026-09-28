def depth_limited_search(state, goal, depth, path):

    if state == goal:
        return path

    if depth == 0:
        return None

    zero = state.index(0)
    row, col = divmod(zero, 3)

    # Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            new_state = tuple(new_state)

            # Avoid going back to a previous state
            if new_state not in path:
                result = depth_limited_search(
                    new_state,
                    goal,
                    depth - 1,
                    path + [new_state]
                )

                if result is not None:
                    return result

    return None


def ids(initial, goal):

    depth = 0

    while True:

        solution = depth_limited_search(
            initial,
            goal,
            depth,
            [initial]
        )

        if solution is not None:
            return solution

        depth += 1


def print_solution(solution):
    if solution is None:
        print("No solution found")
        return

    print("Number of steps:", len(solution) - 1)
    print()

    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()


# 0 represents the blank space
initial = (5, 4, 0,
           6, 1, 8,
           7, 3, 2)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = ids(initial, goal)

print("IDS Solution:")
print_solution(solution)
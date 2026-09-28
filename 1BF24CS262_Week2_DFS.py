def dfs(initial, goal):
    stack = [initial]
    visited = set()
    parent = {initial: None}

    while stack:
        state = stack.pop()

        if state == goal:
            # Reconstruct solution path
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        if state in visited:
            continue

        visited.add(state)

        # Find blank position
        zero = state.index(0)
        row, col = divmod(zero, 3)

        # Up, Down, Left, Right
        moves = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:

                new_zero = new_row * 3 + new_col

                new_state = list(state)

                # Swap blank with neighboring tile
                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]

                new_state = tuple(new_state)

                if new_state not in visited and new_state not in parent:
                    parent[new_state] = state
                    stack.append(new_state)

    return None


def print_solution(solution):

    if solution is None:
        print("No solution found")
        return

    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()

    print("Number of steps:", len(solution) - 1)


# 0 represents the blank space

initial = (
    5, 4, 0,
    6, 1, 8,
    7, 3, 2
)

goal = (
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
)

solution = dfs(initial, goal)

print("DFS Solution:")
print_solution(solution)
import time
from collections import deque

# ----------------- MOVE GENERATOR -----------------
def find_possible_moves(state):
    if '_' in state:
        index = state.index('_')

    if index == 0:
        return [1, 3]
    elif index == 1:
        return [0, 2, 4]
    elif index == 2:
        return [1, 5]
    elif index == 3:
        return [0, 4, 6]
    elif index == 4:
        return [1, 3, 5, 7]
    elif index == 5:
        return [2, 4, 8]
    elif index == 6:
        return [3, 7]
    elif index == 7:
        return [4, 6, 8]
    elif index == 8:
        return [5, 7]
    else:
        return []

# ----------------- BFS ALGORITHM -----------------
def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = {tuple(initial_state)}
    states_explored = 0

    while queue:
        current_state, path = queue.popleft()
        states_explored += 1
        print(f"State #{states_explored}: {current_state}")

        if current_state == goal_state:
            return path, states_explored

        possible_moves_indices = find_possible_moves(current_state)

        for move_index in possible_moves_indices:
            next_state = list(current_state)
            blank_index = next_state.index('_')
            next_state[blank_index], next_state[move_index] = next_state[move_index], next_state[blank_index]

            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                queue.append((next_state, path + [next_state]))

    return None, states_explored

# ----------------- TEST -----------------
initial_state = [1, 2, 3,
                 4, 8, '_',
                 7, 6, 5]

goal_state    = [1, 2, 3,
                 4, 5, 6,
                 7, 8, '_']

# Measure execution time
start_time = time.time()
solution_path, explored = bfs(initial_state, goal_state)
end_time = time.time()

if solution_path is None:
    print("Goal state is not reachable from the initial state.")
else:
    print("\n\nSolution path found:")
    for step, state in enumerate(solution_path, start=1):
        print(f"Step {step}: {state}")

print("\nExecution time: {:.6f} seconds".format(end_time - start_time))
print("Total states explored:", explored)

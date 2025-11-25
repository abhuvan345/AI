import heapq

def state_key(state):
    return ",".join(map(str, state))

def is_solvable(state):
    inversions = 0
    arr = [x for x in state if x != 0]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0

def manhattan(state):
    total = 0
    for index, val in enumerate(state):
        if val == 0:
            continue
        goal_idx = val - 1
        curr_row, curr_col = divmod(index, 3)
        goal_row, goal_col = divmod(goal_idx, 3)
        total += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return total

def get_neighbours(state):
    neighbours = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)
    moves = []
    if row > 0: moves.append(blank_idx - 3)
    if row < 2: moves.append(blank_idx + 3)
    if col > 0: moves.append(blank_idx - 1)
    if col < 2: moves.append(blank_idx + 1)
    for m in moves:
        new_state = list(state)
        new_state[blank_idx], new_state[m] = new_state[m], new_state[blank_idx]
        neighbours.append(tuple(new_state))
    return neighbours

def reconstruct_path(came_from, current_key):
    path = []
    while current_key in came_from:
        path.append(tuple(map(int, current_key.split(","))))
        current_key = came_from[current_key]
    path.append(tuple(map(int, current_key.split(","))))
    path.reverse()
    return path

def a_star(start_state, goal_state):
    if not is_solvable(start_state):
        return "UNSOLVABLE"

    start_key = state_key(start_state)
    goal_key = state_key(goal_state)

    if start_key == goal_key:
        return [start_state]

    open_heap = []
    g_score = {start_key: 0}
    f_score = {start_key: manhattan(start_state)}
    came_from = {}

    heapq.heappush(open_heap, (f_score[start_key], manhattan(start_state), start_state))
    closed = set()

    while open_heap:
        f_current, h_current, current_state = heapq.heappop(open_heap)
        current_key = state_key(current_state)

        if f_current > f_score.get(current_key, float("inf")):
            continue

        if current_key == goal_key:
            return reconstruct_path(came_from, current_key)

        closed.add(current_key)

        for neighbour in get_neighbours(current_state):
            neighbour_key = state_key(neighbour)
            tentative_g = g_score[current_key] + 1

            if neighbour_key in closed and tentative_g >= g_score.get(neighbour_key, float("inf")):
                continue

            if tentative_g < g_score.get(neighbour_key, float("inf")):
                came_from[neighbour_key] = current_key
                g_score[neighbour_key] = tentative_g
                h = manhattan(neighbour)
                f = tentative_g + h
                f_score[neighbour_key] = f
                heapq.heappush(open_heap, (f, h, neighbour))

    return "FAILURE"

if __name__ == "__main__":
    print("Enter start state of the puzzle (9 numbers, 0 for blank space):")
    user_input = input().strip().split()

    if len(user_input) != 9:
        print("Invalid input! Please enter exactly 9 numbers")
        exit()

    try:
        start = tuple(map(int, user_input))
    except ValueError:
        print("Invalid input! Please enter integers only")
        exit()

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

    solution = a_star(start, goal)

    if solution == "UNSOLVABLE":
        print("Puzzle cannot be solved!")
    elif solution == "FAILURE":
        print("No solution found")
    else:
        print("Solution found in", len(solution) - 1, "moves:")
        for state in solution:
            for i in range(0, 9, 3):
                print(state[i:i+3])
            print("-----")

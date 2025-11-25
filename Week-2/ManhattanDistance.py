import heapq

GOAL_STATE = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)


goal_positions = {
    val: (i, j)
    for i, row in enumerate(GOAL_STATE)
    for j, val in enumerate(row)
}

def heuristic(state):
    """Manhattan distance"""
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = goal_positions[val]
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def get_neighbors(state):
    neighbors = []

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def print_state(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()

def a_star_collect_by_depth(start_state):
    start_state = tuple(tuple(row) for row in start_state)
    open_set = []
    heapq.heappush(open_set, (heuristic(start_state), 0, start_state))
    came_from = {}
    g_score = {start_state: 0}
    visited = set()


    popped_by_depth = {}

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        if current in visited:
            continue

        visited.add(current)
        h = heuristic(current)
        f = current_g + h
        popped_by_depth.setdefault(current_g, []).append((f, current))

        if current == GOAL_STATE:
            break

        for neighbor in get_neighbors(current):
            if neighbor in visited:
                continue

            tentative_g = current_g + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    for depth in sorted(popped_by_depth.keys()):
        print(f"\n--- States visited at depth {depth} ---")
        for f, state in popped_by_depth[depth]:
            print(f"f(n): {f}")
            print_state(state)


    if GOAL_STATE in g_score:
        return reconstruct_path(came_from, GOAL_STATE)
    else:
        return None



start_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

path = a_star_collect_by_depth(start_state)

if path:
    print(f"\n Solution found in {len(path) - 1} moves:\n")
    for step in path:
        print_state(step)
else:
    print(" No solution found.")

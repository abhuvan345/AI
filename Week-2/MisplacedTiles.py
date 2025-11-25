import heapq

GOAL_STATE = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)

def heuristic(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                misplaced += 1
    return misplaced

def get_neighbors(state):
    neighbors = []
    x = y = -1
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break
        if x != -1:
            break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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

def a_star(start_state):
    start_state = tuple(tuple(row) for row in start_state)
    open_set = []
    heapq.heappush(open_set, (heuristic(start_state), 0, start_state))
    came_from = {}
    g_score = {start_state: 0}
    visited = set()

    while open_set:
        f_current, current_g, current = heapq.heappop(open_set)


        print(f"Visited depth (g): {current_g}, f(n): {f_current}")
        print_state(current)

        if current == GOAL_STATE:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in visited:
                continue

            tentative_g = current_g + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    return None


start_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

path = a_star(start_state)

if path:
    print(f"Solution found in {len(path) - 1} moves:\n")
    for step in path:
        print_state(step)
else:
    print("No solution found.")

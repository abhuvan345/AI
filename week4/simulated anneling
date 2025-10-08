import random, math

random.seed(42)

def heuristic(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def print_board(state):
    n = len(state)
    for r in range(n):
        print(' '.join('Q' if state[c] == r else '.' for c in range(n)))
    print()

def simulated_annealing(N=4, T0=5.0, alpha=0.95, max_iters=200):
    state = [random.randrange(N) for _ in range(N)]
    cur_h = heuristic(state)
    T = T0

    print_board(state)

    for _ in range(max_iters):
        col = random.randrange(N)
        new_row = random.randrange(N)
        while new_row == state[col]:
            new_row = random.randrange(N)

        new_state = state.copy()
        new_state[col] = new_row
        new_h = heuristic(new_state)
        delta = new_h - cur_h

        if delta <= 0 or random.random() < math.exp(-delta / T):
            state = new_state
            cur_h = new_h
            print_board(state)
            if cur_h == 0:
                break
        T *= alpha

simulated_annealing(4)

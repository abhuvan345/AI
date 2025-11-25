import random
import math

# ----- Helper functions -----

def random_state(n):
    """Generate a random state: one queen per column."""
    return [random.randint(0, n - 1) for _ in range(n)]

def cost(state):
    """Compute the number of attacking pairs of queens (lower is better)."""
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def random_neighbour(state):
    """Generate a neighbour by moving one queen to another row."""
    n = len(state)
    neighbour = state.copy()
    col = random.randint(0, n - 1)      # random column
    new_row = random.randint(0, n - 1)  # new random row
    neighbour[col] = new_row
    return neighbour

# ----- Simulated Annealing -----

def simulated_annealing(n, initial_temp=1000, cooling_rate=0.95, stop_temp=1e-3, max_iterations=10000):
    current = random_state(n)
    current_cost = cost(current)
    T = initial_temp
    iteration = 0

    print("\nInitial state:", current, "Cost:", current_cost)

    while T > stop_temp and iteration < max_iterations:
        next_state = random_neighbour(current)
        next_cost = cost(next_state)
        deltaE = current_cost - next_cost

        # Acceptance condition
        if deltaE > 0:
            accepted = True
        else:
            p = math.exp(deltaE / T)
            accepted = random.random() < p

        # Print current step info
        print(f"\nStep {iteration+1}:")
        print(f"  Current: {current} (Cost={current_cost})")
        print(f"  Next:    {next_state} (Cost={next_cost})")
        print(f"  ΔE = {deltaE:.3f}, T = {T:.3f}")
        print(f"  Accepted: {accepted}")

        # Accept or reject
        if accepted:
            current = next_state
            current_cost = next_cost

        # Cooling
        T *= cooling_rate
        iteration += 1

        # Stop if solved
        if current_cost == 0:
            break

    return current, current_cost, iteration

# ----- Main -----

if __name__ == "__main__":
    n = int(input("Enter the number of queens (N): "))
    solution, cost_val, iterations = simulated_annealing(n)

    print("\nFinal state:", solution)
    print("Conflicts:", cost_val)
    print("Iterations:", iterations)

    if cost_val == 0:
        print("\nSolution found:\n")
        for row in range(n):
            print(" ".join("Q" if solution[col] == row else "." for col in range(n)))
    else:
        print("\nNo perfect solution found (try rerunning; SA is stochastic).")
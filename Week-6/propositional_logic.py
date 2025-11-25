from itertools import product

# Function to safely evaluate logical expressions from user input
def eval_expr(expr, model):
    # Replace logical symbols for Python syntax
    expr = expr.replace('∨', 'or').replace('∧', 'and').replace('¬', 'not ')
    return eval(expr, {}, model)

# Generate all possible truth assignments (models)
def all_models(symbols):
    for values in product([False, True], repeat=len(symbols)):
        yield dict(zip(symbols, values))

# Check entailment: KB ⊨ α
def entails(KB_expr, alpha_expr, symbols):
    for model in all_models(symbols):
        kb_val = eval_expr(KB_expr, model)
        alpha_val = eval_expr(alpha_expr, model)
        if kb_val and not alpha_val:
            print(" Counterexample found:", model)
            return False
    return True

# Display truth table
def truth_table(KB_expr, alpha_expr, symbols):
    headers = "  ".join(f"{s:^6}" for s in symbols)
    print(f"{headers}   {'KB':^8}   {'α':^8}")
    print("-" * (10 * len(symbols) + 20))
    for model in all_models(symbols):
        values = "  ".join(f"{str(model[s]):^6}" for s in symbols)
        kb_val = eval_expr(KB_expr, model)
        alpha_val = eval_expr(alpha_expr, model)
        print(f"{values}   {str(kb_val):^8}   {str(alpha_val):^8}")

# === Main Program ===
print("=== Propositional Entailment using Truth Table Enumeration ===")

# Input propositional variables
symbols = input("Enter propositional symbols (comma separated, e.g., A,B,C): ").replace(" ", "").split(",")

# Input Knowledge Base (KB) and Query (α)
KB_expr = input("Enter Knowledge Base (use and/or/not or ∧/∨/¬): ")
alpha_expr = input("Enter Query α (use and/or/not or ∧/∨/¬): ")

# Display truth table
print("\n--- Truth Table ---")
truth_table(KB_expr, alpha_expr, symbols)

# Check entailment
result = entails(KB_expr, alpha_expr, symbols)
print("\nResult:")
print(" KB entails α" if result else " KB does NOT entail α")


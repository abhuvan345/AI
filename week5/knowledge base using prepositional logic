from itertools import product

# Define propositional symbols
symbols = ['P', 'Q', 'R']

# Define the KB sentences as functions on the model dict
def sentence1(model):
    # Q -> P
    Q = model['Q']
    P = model['P']
    return (not Q) or P

def sentence2(model):
    # P -> ¬Q
    P = model['P']
    Q = model['Q']
    return (not P) or (not Q)

def sentence3(model):
    # Q ∨ R
    Q = model['Q']
    R = model['R']
    return Q or R

def KB(model):
    return sentence1(model) and sentence2(model) and sentence3(model)

def entails(KB, query, symbols):
    """
    Check if KB entails query by enumerating all models.
    Returns True if for every model where KB is True, query is True.
    """
    for values in product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        if KB(model) and not query(model):
            # Found a model where KB is true but query false
            return False
    return True

# Queries to test
def query_R(model):
    return model['R']

def query_R_implies_P(model):
    R = model['R']
    P = model['P']
    return (not R) or P

def query_Q_implies_R(model):
    Q = model['Q']
    R = model['R']
    return (not Q) or R

# Print truth table rows where KB is True
print("Models where KB is true:")
for values in product([True, False], repeat=len(symbols)):
    model = dict(zip(symbols, values))
    if KB(model):
        print(model)

# Check entailments
print("\nDoes KB entail R? ", entails(KB, query_R, symbols))
print("Does KB entail R -> P? ", entails(KB, query_R_implies_P, symbols))
print("Does KB entail Q -> R? ", entails(KB, query_Q_implies_R, symbols))

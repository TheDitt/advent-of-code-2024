from itertools import product

def generate_operator_combinations(num_operators):
    """Generate all combinations of '+' and '*' for the
                         given number of operator positions."""
    return list(product('+*|', repeat=num_operators))
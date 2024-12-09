import generate_operator_combinations

def test_generate_operator_combinations():
    # Test case 1: Zero operators
    num_operators = 0
    expected_combinations = [()]
    assert generate_operator_combinations.generate_operator_combinations(
        num_operators) == expected_combinations, "Test case 1 failed"

    # Test case 2: One operator
    num_operators = 1
    expected_combinations = [('+',), ('*',), ('|',)]
    
    assert generate_operator_combinations.generate_operator_combinations(
        num_operators) == expected_combinations, "Test case 2 failed"

    # Test case 3: Two operators
    num_operators = 2
    expected_combinations = [
        ('+', '+'), ('+', '*'), 
        ('+', '|'), ('*', '+'), 
        ('*', '*'), ('*', '|'), 
        ('|', '+'), ('|', '*'), 
        ('|', '|')
        ]
    
    assert generate_operator_combinations.generate_operator_combinations(
        num_operators) == expected_combinations, "Test case 3 failed"

    # Test case 4: Three operators
    num_operators = 3
    expected_combinations = [
        ('+', '+', '+'), ('+', '+', '*'), ('+', '+', '|'), 
        ('+', '*', '+'), ('+', '*', '*'), ('+', '*', '|'), 
        ('+', '|', '+'), ('+', '|', '*'), ('+', '|', '|'), 
        ('*', '+', '+'), ('*', '+', '*'), ('*', '+', '|'),
        ('*', '*', '+'), ('*', '*', '*'), ('*', '*', '|'), 
        ('*', '|', '+'), ('*', '|', '*'), ('*', '|', '|'), 
        ('|', '+', '+'), ('|', '+', '*'), ('|', '+', '|'), 
        ('|', '*', '+'), ('|', '*', '*'), ('|', '*', '|'), 
        ('|', '|', '+'), ('|', '|', '*'), ('|', '|', '|')
        ]
    
    assert generate_operator_combinations.generate_operator_combinations(
        num_operators) == expected_combinations, "Test case 4 failed"

    print("All test cases for generate_operator_combinations passed!")

# Run the test cases
test_generate_operator_combinations()

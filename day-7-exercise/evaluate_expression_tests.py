import evaluate_expression

def test_evaluate_expression():
    # Test case 1: Simple addition
    numbers = [1, 2, 3]
    operators = ['+', '+']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 6, "Test case 1: Simple addition - Failed"

    # Test case 2: Simple multiplication
    numbers = [2, 3, 4]
    operators = ['*', '*']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 24, "Test case 2: Simple multiplication - Failed"

     # Test case 3: Simple concatenation
    numbers = [2, 3, 4]
    operators = ['|', '|']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 234, "Test case 3: Simple concatenation - Failed"

    # Test case 4: Mixed operators, left to right
    numbers = [2, 3, 4]
    operators = ['+', '*']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 20, "Test case 4: Mixed operators, \
                                                    left to right - Failed"

    # Test case 5: Mixed operators, left to right
    numbers = [2, 3, 4]
    operators = ['*', '+']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 10, "Test case 5: Mixed operators, \
                                                     left to right - Failed"

    # Test case 6: Mixed operators, left to right
    numbers = [2, 3, 4]
    operators = ['|', '+']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 27, "Test case 6: Mixed operators, \
                                                     left to right - Failed"
    
    # Test case 7: Mixed operators, left to right
    numbers = [2, 3, 4]
    operators = ['*', '|']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 64, "Test case 7: Mixed operators, \
                                                     left to right - Failed"
    
    # Test case 8: Single number, no operators
    numbers = [5]
    operators = []
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 5, "Test case 8: Single number, no operators - Failed"

    # Test case 9: All addition
    numbers = [10, 20, 30, 40]
    operators = ['+', '+', '+']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 100, "Test case 9: All addition - Failed"

    # Test case 10: All multiplication
    numbers = [1, 2, 3, 4]
    operators = ['*', '*', '*']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 24, "Test case 10: All multiplication - Failed"
    
    # Test case 11: All concatenation
    numbers = [1, 2, 3, 4]
    operators = ['|', '|', '|']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 1234, "Test case 11: All concatenation - Failed"
    
    # Test case 12: Complex mixed operators
    numbers = [5, 1, 2, 3]
    operators = ['|', '*', '+']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 105, "Test case 12: Complex mixed operators - Failed"
    
    # Test case 13: Zero multiplication
    numbers = [5, 0, 3]
    operators = ['*', '+']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 3, "Test case 13: Zero multiplication - Failed"

    # Test case 13: Zero addition
    numbers = [5, 0, 3]
    operators = ['+', '*']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 15, "Test case 13: Zero addition - Failed"
    
     # Test case 14: Zero concatenation
    numbers = [5, 0, 3]
    operators = ['|', '*']
    assert evaluate_expression.evaluate_expression(
        numbers, operators) == 150, "Test case 14: Zero concatentation - Failed"

    print("All test cases passed!")

# Run the test cases
test_evaluate_expression()

def evaluate_expression(numbers, operators):
    """Evaluate the expression formed by numbers and operators from left to right."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '|':
            result = int(str(result) + str(numbers[i + 1]))
    
    return result
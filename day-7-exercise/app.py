import evaluate_expression
import generate_operator_combinations

# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
input_data = my_file.read()

equations = []
for line in input_data.strip().split('\n'):
    equations.append(line)

def find_valid_equations(equations):
    total_calibration_result = 0

    for equation in equations:
        parts = equation.split(':')
        target = int(parts[0].strip())
        numbers = list(map(int, parts[1].strip().split()))

        # Generate all combinations of '+' and '*' for the operators
        num_operators = len(numbers) - 1
        for ops in generate_operator_combinations.generate_operator_combinations(
            num_operators):
            if evaluate_expression.evaluate_expression(numbers, ops) == target:
                total_calibration_result += target
                break  # No need to check further if one valid expression is found

    return total_calibration_result

# Calculate the total calibration result
result = find_valid_equations(equations)
print("Total Calibration Result:", result)

my_file.close()
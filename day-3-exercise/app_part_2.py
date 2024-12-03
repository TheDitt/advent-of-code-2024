import re

# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read()

def evaluate_expression(expression):
    # Regular expression to find all mul(X, Y) patterns
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    
    # Split the expression into parts based on instructions
    parts = re.split(r'(do\(\)|don\'t\(\)|undo\(\))', expression)
    
    # Initialize a flag to determine whether to apply multiplication
    apply_mul = True
    
    # Initialize a variable to store the total sum
    total_sum = 0
    
    # Iterate over each part of the expression
    for part in parts:
        part = part.strip()
        
        if part == 'do()':
            apply_mul = True
        elif part == "don't()":
            apply_mul = False
        elif part == 'undo()':
            apply_mul = not apply_mul
        else:
            # Find all mul(X, Y) in the current part
            for match in mul_pattern.finditer(part):
                x, y = int(match.group(1)), int(match.group(2))
                
                # Apply multiplication only if the flag is set
                if apply_mul:
                    total_sum += x * y
    
    return total_sum

# Evaluate the expression
result = evaluate_expression(data)

# Print the result
print("Total sum of applicable multiplications:", result)

my_file.close() 
import re

# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read()

# Regular expression pattern to match mul(X,Y)
pattern = r'mul\(\d+,\d+\)'

# Find all matches in the input string
expressions = re.findall(pattern, data)

# Print the matches
print(expressions)

# Initialize a variable to store the sum of all multiplications
total_sum = 0

# Iterate over each expression in the array
for expr in expressions:
    # Extract the numbers from the expression
    numbers = expr[4:-1].split(',')
    x, y = int(numbers[0]), int(numbers[1])
    
    # Compute the multiplication
    result = x * y
    
    # Add the result to the total sum
    total_sum += result

# Print the total sum of all multiplications
print("Total sum of multiplications:", total_sum)

my_file.close() 
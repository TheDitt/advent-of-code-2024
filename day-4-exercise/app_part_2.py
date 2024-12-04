# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read()

# Split the text into lines and filter out any empty lines
grid = [list(line) for line in data.strip().split('\n')]

def search_pattern(grid, pattern):
    rows = len(grid)
    cols = len(grid[0])
    pattern_rows = len(pattern)
    pattern_cols = len(pattern[0])

    def matches_pattern(x, y):
        for i in range(pattern_rows):
            for j in range(pattern_cols):
                if pattern[i][j] != '.' and grid[x + i][y + j] != pattern[i][j]:
                    return False
        return True

    count = 0
    for x in range(rows - pattern_rows + 1):
        for y in range(cols - pattern_cols + 1):
            if matches_pattern(x, y):
                count += 1

    return count

def search_multiple_patterns(grid, patterns):
    results = {}
    for pattern in patterns:
        count = search_pattern(grid, pattern)
        results[tuple(map(tuple, pattern))] = count
    return results

# Define the patterns
patterns = [
    [
        ['M', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'S']
    ],
    [
        ['S', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'M']
    ],
    [
        ['M', '.', 'M'],
        ['.', 'A', '.'],
        ['S', '.', 'S']
    ],
    [
        ['S', '.', 'M'],
        ['.', 'A', '.'],
        ['S', '.', 'M']
    ]
]

# Search for all patterns
results = search_multiple_patterns(grid, patterns)

# Print the results
total = 0
for pattern, count in results.items():
    print(f"The pattern {pattern} appears {count} times in the grid.")
    total += count

print(f"Total: {total}")

my_file.close() 
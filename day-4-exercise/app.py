# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read()

# Split the text into lines and filter out any empty lines
grid = [list(line) for line in data.strip().split('\n')]

# Print the resulting array
print(grid)

def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Directions: right, left, down, up, diagonal down-right, diagonal down-left, diagonal up-right, diagonal up-left
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1

    return count

# Count occurrences of "XMAS"
word = "XMAS"
occurrences = count_word_occurrences(grid, word)
print(f"The word '{word}' appears {occurrences} times in the grid.")

my_file.close() 
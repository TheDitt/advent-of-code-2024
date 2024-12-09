# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
input_data = my_file.read()

map_input = []
for line in input_data.strip().split('\n'):
    map_input.append(line)


def simulate_guard_path(map_data):
    # Parse the map and find the initial position and direction of the guard
    directions = ['^', '>', 'v', '<']
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    guard_pos = None
    guard_dir = None
    
    # Find the guard's initial position and direction
    for r, row in enumerate(map_data):
        for c, char in enumerate(row):
            if char in directions:
                guard_pos = (r, c)
                guard_dir = directions.index(char)
                break
        if guard_pos:
            break
    
    # Set to track visited positions
    visited_positions = set()
    visited_positions.add(guard_pos)
    
    # Map dimensions
    max_row = len(map_data)
    max_col = len(map_data[0])
    
    # Simulate the guard's movement
    while True:
        # Calculate the next position
        move = moves[guard_dir]
        next_pos = (guard_pos[0] + move[0], guard_pos[1] + move[1])
        
        # Check if the next position is within bounds
        if (0 <= next_pos[0] < max_row) and (0 <= next_pos[1] < max_col):
            # Check if the next position is an obstacle
            if map_data[next_pos[0]][next_pos[1]] == '#':
                # Turn right
                guard_dir = (guard_dir + 1) % 4
            else:
                # Move forward
                guard_pos = next_pos
                visited_positions.add(guard_pos)
        else:
            # The guard has left the map
            break
    
    # Return the number of distinct positions visited
    return len(visited_positions)

# Calculate the number of distinct positions visited
# distinct_positions_visited = simulate_guard_path(map_input)
# print(distinct_positions_visited)

def find_obstruction_positions(map_data):
    # Define movement directions and right turn mapping
    directions = ['^', '>', 'v', '<']
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    # Find the initial position and direction of the guard
    guard_pos = None
    guard_dir = None
    for r, row in enumerate(map_data):
        for c, char in enumerate(row):
            if char in directions:
                guard_pos = (r, c)
                guard_dir = char
                break
        if guard_pos:
            break
    
    # Map dimensions
    max_row = len(map_data)
    max_col = len(map_data[0])
    
    # Track visited positions with direction
    visited = {}
    cycle_positions = set()
    
    # Simulate the guard's movement
    while True:
        # Calculate the next position
        dr, dc = moves[directions.index(guard_dir)]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)
        
        # Check if the next position is within bounds and not an obstacle
        if (0 <= next_pos[0] < max_row and 0 <= next_pos[1] < max_col and
                map_data[next_pos[0]][next_pos[1]] != '#'):
            # Move to the next position
            guard_pos = next_pos
        else:
            # Turn right
            guard_dir = turn_right[guard_dir]
        
        # Check if the guard has left the map
        if not (0 <= guard_pos[0] < max_row and 0 <= guard_pos[1] < max_col):
            break
        
        # Check for cycles
        state = (guard_pos, guard_dir)
        if state in visited:
            # Cycle detected, add positions to cycle_positions
            cycle_start = visited[state]
            for pos in list(visited.keys())[cycle_start:]:
                cycle_positions.add(pos[0])
            break
        else:
            visited[state] = len(visited)
    
    # Remove the guard's starting position from possible obstruction positions
    cycle_positions.discard((guard_pos[0], guard_pos[1]))
    
    # Return the number of valid obstruction positions
    return len(cycle_positions)

# # Example map input
# map_input = [
#     "....#.....",
#     ".........#",
#     "..........",
#     "..#.......",
#     ".......#..",
#     "..........",
#     ".#..^.....",
#     "........#.",
#     "#.........",
#     "......#..."
# ]

# Calculate the number of possible obstruction positions
obstruction_positions_count = find_obstruction_positions(map_input)
print(obstruction_positions_count)

my_file.close()
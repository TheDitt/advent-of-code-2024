from collections import defaultdict, deque

# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
input_data = my_file.read()

def parse_input(input_data):
    lines = input_data.strip().split('\n')
    rules = []
    updates = []
    parsing_rules = True

    for line in lines:
        if line.strip() == "":
            parsing_rules = False
            continue
        if parsing_rules:
            rules.append(tuple(map(int, line.split('|'))))
        else:
            updates.append(list(map(int, line.split(','))))

    return rules, updates

def is_update_correct(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def find_middle_page(update):
    middle_index = len(update) // 2
    return update[middle_index]

def reorder_update(update, rules):
    # Create a graph to represent dependencies
    graph = defaultdict(list)
    indegree = {page: 0 for page in update}

    # Build the graph based on the rules
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            indegree[y] += 1

    # Perform topological sort
    queue = deque([page for page in update if indegree[page] == 0])
    sorted_update = []

    while queue:
        page = queue.popleft()
        sorted_update.append(page)
        for neighbor in graph[page]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def sum_middle_pages_of_correct_updates(rules, updates):
    correct_updates = [update for update in updates if is_update_correct(update, rules)]
    middle_pages = [find_middle_page(update) for update in correct_updates]
    return sum(middle_pages)

def sum_middle_pages_of_reordered_updates(rules, updates):
    incorrect_updates = [update for update in updates 
                         if not is_update_correct(update, rules)]
    reordered_updates = [reorder_update(update, rules) for update in incorrect_updates]
    [print(update) for update in reordered_updates]
    middle_pages = [find_middle_page(update) for update in reordered_updates]

    return sum(middle_pages)

# Parse the input data
rules, updates = parse_input(input_data)

# Calculate the sum of middle pages of correctly ordered updates
correct_order_result = sum_middle_pages_of_correct_updates(rules, updates)

# Calculate the sum of middle pages of reordered incorrectly ordered updates
incorrect_order_result = sum_middle_pages_of_reordered_updates(rules, updates)

print("Sum of middle page numbers from correctly ordered updates:"
        , correct_order_result)
print("Sum of middle page numbers after correctly ordering the incorrect updates:"
        , incorrect_order_result)

my_file.close()
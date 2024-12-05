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

def sum_middle_pages_of_correct_updates(rules, updates):
    correct_updates = [update for update in updates if is_update_correct(update, rules)]
    middle_pages = [find_middle_page(update) for update in correct_updates]
    return sum(middle_pages)

# Parse the input data
rules, updates = parse_input(input_data)

# Calculate the sum of middle pages of correctly ordered updates
result = sum_middle_pages_of_correct_updates(rules, updates)

print("Sum of middle page numbers from correctly ordered updates:", result)

my_file.close()
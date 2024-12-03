# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read()

# Split the string into lines and then split each line into integers
list_of_lists = [list(map(int, line.split())) for line in data.strip().split('\n')]

print(list_of_lists)

def check_sequencing(array):
    is_increasing = True
    is_decreasing = True

    for i in range(1, len(array)):
        if array[i] <= array[i - 1]:
            is_increasing = False
        if array[i] >= array[i - 1]:
            is_decreasing = False
    
    if not is_increasing and not is_decreasing:
        return True
    else: 
        return False


safe_count = 0
for list in list_of_lists:
   
    list_safe = True
    for i in range(1, len(list)):
        current_number = list[i]
        last_number = list[i - 1]
        difference = abs(current_number - last_number)
        
        if difference > 3:
            list_safe = False
        elif difference == 0:
            list_safe = False

        if check_sequencing(list):
            list_safe = False


    if list_safe:
        safe_count += 1

print(f"Safe Count: {safe_count}")

my_file.close() 
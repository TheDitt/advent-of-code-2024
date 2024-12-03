# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read()

# Split the string into lines and then split each line into integers
list_of_lists = [list(map(int, line.split())) for line in data.strip().split('\n')]

print(list_of_lists)

answer = 0

for line in list_of_lists:

    is_increasing = None
    for i in range(0, len(line) - 1):
        a = line[i]
        b = line[i + 1]

        if a > b:
            if is_increasing is None:
                is_increasing = False
            elif is_increasing:
                break
        else:
            if is_increasing is None:
                is_increasing = True
            elif not is_increasing:
                break

        diff = abs(a - b)
        if diff < 1 or diff > 3:
            break
    else:
        answer += 1
        continue

    # Brute force, try it with each number removed
    for j in range(0, len(line)):
        new_row = line[:j] + line[j + 1 :]
        is_increasing = None
        for i in range(0, len(new_row) - 1):
            a = new_row[i]
            b = new_row[i + 1]

            if a > b:
                if is_increasing is None:
                    is_increasing = False
                elif is_increasing:
                    break
            else:
                if is_increasing is None:
                    is_increasing = True
                elif not is_increasing:
                    break

            diff = abs(a - b)
            if diff < 1 or diff > 3:
                break
        else:
            answer += 1
            break

print(f"Part 2: {answer}")

my_file.close() 
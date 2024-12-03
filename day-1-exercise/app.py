import re

# opening the file in read mode 
# my_file = open("test_input.txt", "r") 
my_file = open("input.txt", "r") 
  
# reading the file 
data = my_file.read() 

# abstract data
lines = data.strip().split('\n')
list1, list2 = [], []

for line in lines:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

# Sort the lists in order
list1.sort()
list2.sort()
print("List 1:", list1)
print("List 2:", list2)

total = 0
for num1, num2 in zip(list1, list2):
    diff = 0
    if num2 > num1:
        diff = num2 - num1
    else:
        diff = num1-num2

    print(diff)
    total = total + diff

print(f"Total: {total}")

my_file.close() 
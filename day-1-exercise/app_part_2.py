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
print("List 1:", list1)
print("List 2:", list2)

similarity_score_total = 0
for num in list1:
    occurences = list2.count(num)
    similarity_score = num * occurences

    similarity_score_total = similarity_score_total + similarity_score

print(f"Similarity Score: {similarity_score_total}")

my_file.close() 
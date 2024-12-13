import garden_map as gm
import garden_map_2 as gm2

# opening the file in read mode 
my_file = open("input.txt", "r") 
  
# reading the file 
input_data = my_file.read()

map_data = []
for line in input_data.strip().split('\n'):
    map_data.append(line)

garden_map = gm.GardenMap(map_data)
total_price = garden_map.calculate_total_price()
print(f"Total price of fencing all regions: {total_price}")



my_file.close()
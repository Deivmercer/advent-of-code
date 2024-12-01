left_list = list()
right_list = list()
file_name = "input.txt"
with open(file_name, "r") as input_file:
    for line in input_file:
        split = line.split("   ")
        left_list += [int(split[0])]
        right_list += [int(split[1])]

total_distance = 0
left_list.sort()
right_list.sort()
for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])
print(total_distance)

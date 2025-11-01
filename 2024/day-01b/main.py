left_list = list()
right_list = list()
file_name = "input.txt"
with open(file_name, "r") as input_file:
    for line in input_file:
        split = line.split("   ")
        left_list += [int(split[0])]
        right_list += [int(split[1])]

occurences = dict()
for n in right_list:
    occurences[n] = occurences[n] + 1 if n in occurences else 1

similarity = 0
for n in left_list:
    similarity += n * (occurences[n] if n in occurences else 0)
print(similarity)

result = 0
file_name = "input.txt"
with open(file_name, "r") as input_file:
    for line in input_file:
        split = line.split("mul(")
        for el in split:
            split = el.split(")")
            try:
                [a, b] = split[0].split(",")
                result += int(a) * int(b)
            except:
                pass
print(result)

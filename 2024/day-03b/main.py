result = 0
enabled = True
file_name = "input.txt"
with open(file_name, "r") as input_file:
    for line in input_file:
        remaining = line
        while "mul(" in remaining:
            mul_occurrance = remaining.find("mul(")
            do_occurrance = remaining.find("do()") if "do()" in remaining else 9999
            dont_occurrance = remaining.find("don't()") if "don't()" in remaining else 9999
            if do_occurrance < mul_occurrance and do_occurrance < dont_occurrance:
                enabled = True
            elif dont_occurrance < mul_occurrance and dont_occurrance < do_occurrance:
                enabled = False
            if enabled:
                split = remaining.split("mul(")[1].split(")")[0]
                try:
                    [a, b] = split.split(",")
                    result += int(a) * int(b)
                except:
                    pass
            remaining = remaining[mul_occurrance + 4:]
print(result)

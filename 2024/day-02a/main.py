safe_reports = 0
file_name = "input2.txt"
with open(file_name, "r") as input_file:
    for line in input_file:
        split = line.strip().split(" ")
        split = [int(el) for el in split]
        prev = split[0]
        unsafe = False
        if split[0] > split[1]:
            for el in split[1:]:
                diff = prev - el
                if el > prev or diff < 1 or diff > 3:
                    unsafe = True
                    break
                prev = el
        else:
            for el in split[1:]:
                diff = el - prev
                if el < prev or diff < 1 or diff > 3:
                    unsafe = True
                    break
                prev = el
        if not unsafe:
            safe_reports += 1
print(safe_reports)

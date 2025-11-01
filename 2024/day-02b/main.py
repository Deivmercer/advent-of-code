def is_safe(levels, first=False):
    unsafe = -1
    prev = levels[0]
    if levels[0] > levels[1]:
        for i in range(len(levels))[1:]:
            diff = prev - levels[i]
            if levels[i] > prev or diff < 1 or diff > 3:
                unsafe = i
                break
            prev = levels[i]
    else:
        for i in range(len(levels))[1:]:
            diff = levels[i] - prev
            if levels[i] < prev or diff < 1 or diff > 3:
                unsafe = i
                break
            prev = levels[i]
    if unsafe != -1:
        if first:
            unsafe -= 1
            dampener = is_safe(levels[:unsafe - 1] + levels[unsafe:])
            dampener = dampener or is_safe(levels[:unsafe] + levels[unsafe + 1:])
            dampener = dampener or is_safe(levels[:unsafe + 1] + levels[unsafe + 2:])
            return dampener
        else:
            return False
    return True

safe_reports = 0
file_name = "input.txt"
with open(file_name, "r") as input_file:
    for line in input_file:
        split = line.strip().split(" ")
        split = [int(el) for el in split]
        if is_safe(split, True):
            safe_reports += 1
print(safe_reports)

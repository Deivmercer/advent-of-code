rules = dict()
file_name = "input.txt"
with open(file_name, "r") as input_file:
    input_rows = input_file.readlines()

for i in range(len(input_rows)):
    if input_rows[i] == "\n":
        break
    split = input_rows[i].split("|")
    if split[0] not in rules:
        rules[split[0]] = list()
    rules[split[0]] += [split[1].rstrip()]

result = 0
for j in range(len(input_rows))[i + 1:]:
    pages = input_rows[j].split(",")
    incorrect = False
    x = 0
    while x < len(pages):
        page_i = x
        page = pages[x]
        for y in range(len(pages))[x + 1:]:
            new_page = pages[y].rstrip()
            if new_page in rules and page in rules[new_page] and not y == len(pages):
                pages = pages[:page_i] + [new_page, page] + pages[page_i + 1 : y] + pages[y + 1:]
                page_i += 1
                incorrect = True
        if page_i == x:
            x += 1
    if incorrect:
        middle = int(len(pages) / 2)
        result += int(pages[middle : middle + 1][0])

print(result)

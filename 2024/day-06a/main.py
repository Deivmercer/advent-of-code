file_name = "input.txt"
with open(file_name, "r") as input_file:
    input_rows = input_file.readlines()

position = [0, -1]
for row in input_rows:
    position[1] = row.find("^")
    if position[1] == -1:
        position[0] += 1
    else:
        break

visited = list()
direction = 0
inside = True
next_char_pos = position
while inside:
    if not position in visited:
        visited += [[position[0], position[1]]]
    if input_rows[next_char_pos[0]][next_char_pos[1]] == "#":
        direction = (direction + 1) % 4
    match direction:
        case 0:
            position[0] -= 1
            next_char_pos = [position[0] - 1, position[1]]
        case 1:
            position[1] += 1
            next_char_pos = [position[0], position[1] + 1]
        case 2:
            position[0] += 1
            next_char_pos = [position[0] + 1, position[1]]
        case 3:
            position[1] -= 1
            next_char_pos = [position[0], position[1] - 1]
    inside = 0 <= next_char_pos[0] < len(input_rows) and 0 <= next_char_pos[1] < len(input_rows[position[0]])
print(len(visited) + 1)

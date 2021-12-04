import re

file_name = "input.txt"
with open(file_name, 'r') as input_file:
    input_file_rows = input_file.readlines()

drawn_numbers = input_file_rows[0].split(',')
boards = []
index = -1
for row in input_file_rows[1:]:
    if row != '\n':
        boards[index] += [re.split("\\s+", row.strip())]
    else:
        index += 1
        boards += [[]]

number_found = False
winning_row = [-1] * len(boards[0][0])
winning_board = []
winning_number = -1
for drawn_number in drawn_numbers:
    for board in boards:
        number_found = False
        for row in board:
            for index, number in enumerate(row):
                if number == drawn_number:
                    row[index] = -1
                    number_found = True
                    if row == winning_row:
                        winning_board = board
                        winning_number = number
                    else:
                        j = 0
                        while j < len(board) and board[j][index] == -1:
                            j += 1
                        if j == len(board):
                            winning_board = board
                        winning_number = number
                    break
            if number_found:
                break
        if winning_board:
            break
    if winning_board:
        break

score = 0
for row in winning_board:
    for number in row:
        if number != -1:
            score += int(number)

print(score * int(winning_number))

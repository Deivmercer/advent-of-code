WORD = "MAS"
word_count = 0
file_name = "input.txt"
with open(file_name, "r") as input_file:
    input_rows = input_file.readlines()

for i in range(len(input_rows)):
    input_rows[i] = input_rows[i].strip()
    for j in range(len(input_rows[i])):
        if input_rows[i][j] == WORD[1] and 0 < i < len(input_rows) - 1 and 0 < j < len(input_rows[i]) - 1:
            diag_1 = input_rows[i - 1][j - 1] + WORD[1] + input_rows[i + 1][j + 1]
            diag_2 = input_rows[i - 1][j + 1] + WORD[1] + input_rows[i + 1][j - 1]
            if (diag_1 == WORD or diag_1[::-1] == WORD) and (diag_2 == WORD or diag_2[::-1] == WORD):
                word_count += 1
print(word_count)
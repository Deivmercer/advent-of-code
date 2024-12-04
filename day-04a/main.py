WORD = "XMAS"
word_count = 0
file_name = "input.txt"
with open(file_name, "r") as input_file:
    input_rows = input_file.readlines()

for i in range(len(input_rows)):
    input_rows[i] = input_rows[i].strip()
    for j in range(len(input_rows[i])):
        if input_rows[i][j] == WORD[0]:
            if j > 2 and input_rows[i][j - 3 : j + 1] == WORD[::-1]:
                word_count += 1
            if j < len(input_rows[i]) - 3 and input_rows[i][j : j + 4] == WORD:
                word_count += 1
            if i > 2:
                test = WORD[0] + input_rows[i - 1][j] + input_rows[i - 2][j] + input_rows[i - 3][j]
                if test == WORD:
                    word_count += 1
            if i < len(input_rows) - 3:
                test = WORD[0] + input_rows[i + 1][j] + input_rows[i + 2][j] + input_rows[i + 3][j]
                if test == WORD:
                    word_count += 1
            if i > 2 and j > 2:
                test = WORD[0] + input_rows[i - 1][j - 1] + input_rows[i - 2][j - 2] + input_rows[i - 3][j - 3]
                if test == WORD:
                    word_count += 1
            if i > 2 and j < len(input_rows[i]) - 3:
                test = WORD[0]  + input_rows[i - 1][j + 1] + input_rows[i - 2][j + 2] + input_rows[i - 3][j + 3]
                if test == WORD:
                    word_count += 1
            if i < len(input_rows) - 3 and j > 2:
                test = WORD[0] + input_rows[i + 1][j - 1] + input_rows[i + 2][j - 2] + input_rows[i + 3][j - 3]
                if test == WORD:
                    word_count += 1
            if i < len(input_rows) - 3 and j < len(input_rows[i]) - 3:
                test = WORD[0] + input_rows[i + 1][j + 1] + input_rows[i + 2][j + 2] + input_rows[i + 3][j + 3]
                if test == WORD:
                    word_count += 1
print(word_count)
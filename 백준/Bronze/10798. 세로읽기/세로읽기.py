word = [list(input()) for _ in range(5)]
word_row = 0
word_col = 0
new_word = ""

max_length = max(len(w) for w in word)

for col in range(max_length):
    for row in range(5):
        if col < len(word[row]):
            new_word += word[row][col]

print(new_word)
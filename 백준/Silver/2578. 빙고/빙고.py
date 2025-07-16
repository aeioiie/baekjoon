CS = [list(map(int, input().split())) for _ in range(5)]
SJ = [list(map(int, input().split())) for _ in range(5)]
called_numbers = [num for row in SJ for num in row]

def check_bingo(board):
    count = 0
    for row in board:
        if sum(row) == 0:
            count += 1
    for col in range(5):
        if sum(board[i][col] for i in range(5)) == 0:
            count += 1
    if sum(board[i][i] for i in range(5)) == 0:
        count += 1
    if sum(board[i][4-i] for i in range(5)) == 0:
        count += 1
    return count

called = 0
for num in called_numbers:
    called += 1
    for i in range(5):
        for j in range(5):
            if CS[i][j] == num:
                CS[i][j] = 0
    if check_bingo(CS) >= 3:
        print(called)
        exit()
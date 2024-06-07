def palindrome(string):
    n = len(string)
    for s in range(n // 2):
        if string[s] != string[n - 1 - s]:
            return 0
    return 1


for tc in range(10):
    T = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    length = 1
    word = ''
    for i in range(100):  # 행 번호
        for j in range(length, 101):  # 회문 길이
            for k in range(101 - j):  # 열 번호
                for m in range(k, k + j): # 단어를 저장
                    word += arr[i][m]
                if palindrome(word):
                    temp = len(word)
                    if length < temp:
                        length = temp
                else:
                    word = ''
    for i in range(100):  # 열 번호
        for j in range(length, 101):  # 회문 길이
            for k in range(101 - j):  # 행 번호
                for m in range(k, k + j): # 단어를 저장
                    word += arr[m][i]
                if palindrome(word):
                    temp = len(word)
                    if length < temp:
                        length = temp
                else:
                    word = ''
    print('#{0} {1}'.format(T, length))
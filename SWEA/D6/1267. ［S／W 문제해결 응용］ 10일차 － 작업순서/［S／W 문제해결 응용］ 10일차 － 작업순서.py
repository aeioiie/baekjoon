for tc in range(1, 11):
    v, e = map(int, input().split())
    MyMap = [[0] * (v + 1) for _ in range(v + 1)]
    visited = []

    Data = list(map(int, input().split()))
    N = int(len(Data) / 2)

    for i in range(N):
        row = Data[i * 2]
        col = Data[i * 2 + 1]
        MyMap[col][row] = 1

    result = []
    while True:
        if len(result) == v:
            break

        start_col = []
        for col in range(1, len(MyMap)):
            if 1 not in MyMap[col] and col not in result:
                start_col.append(col)

        for col in start_col:
            result.append(col)
            for row in range(len(MyMap)):
                MyMap[row][col] = 0

    print(f'#{tc}', end=" ")
    for i in result:
        print(f'{i}', end=" ")
    print()
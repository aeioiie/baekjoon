N, M = map(int, input().split())
inputarray = []

for i in range(N):
    horizontal = list(input())
    inputarray.append(horizontal)

max_area = 1

for i in range(N):
    for j in range(M):
        for k in range(1, min(N, M)):
            if i + k < N and j + k < M:
                a = inputarray[i][j]
                b = inputarray[i][j+k]
                c = inputarray[i+k][j]
                d = inputarray[i+k][j+k]
                if a == b == c == d:
                    max_area = max(max_area, (k+1)**2)

print(max_area)
N, M = map(int, input().split())
inputarray = []

for i in range(N):
    inputarray.append([])
    horizontal = list(input())
    inputarray[i] = horizontal

# inputarray = [list(input()) for _ in range(N)]

# print(inputarray)

WBarray = [[], [], [], [], [], [], [], []]
BWarray = [[], [], [], [], [], [], [], []]

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            WBarray[i].append('W')
            BWarray[i].append('B')
        else:
            WBarray[i].append('B')
            BWarray[i].append('W')

# print(WBarray)
# print(BWarray)

min_diff = 999999

for i in range(N-7):
    for j in range(M-7):
        WBdiff = 0
        BWdiff = 0

        for k in range(8):
            for l in range(8):
                if inputarray[i+k][j+l] != WBarray[k][l]:
                    WBdiff += 1
                if inputarray[i+k][j+l] != BWarray[k][l]:
                    BWdiff += 1
        
        min_diff = min(min_diff, WBdiff, BWdiff)

print(min_diff)
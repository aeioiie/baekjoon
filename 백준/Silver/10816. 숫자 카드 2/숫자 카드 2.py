N = int(input())
cards = list(map(int, input().split()))
M = int(input())
how_many = map(int, input().split())

# for i in how_many:
#     count = 0
#     for j in cards:
#         if i == j:
#             count += 1
#     print(count, end=' ')

# 이렇게 하면 시간 초과
# dictionary 사용해서 시간 줄임

compress = {}

for i in cards:
    if i in compress:
        compress[i] += 1
    else:
        compress[i] = 1

for i in how_many:
    if i in compress:
        print(compress[i], end=' ')
    else:
        print(0, end=' ')
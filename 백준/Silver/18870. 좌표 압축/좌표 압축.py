N = int(input())
num = list(map(int, input().split()))
sorted_num = sorted(set(num))

# num = [2, 4, -10, 4, -9]
# sorted_num = [-10, -9, 2, 4, 4]
# print: 2 3 0 3 1

# for i in num:
#     for j in sorted_num:
#         if i == j:
#             print(sorted_num.index(j), end=' ')

# 이렇게 하면 시간 초과
# dictionary 사용해서 시간 줄임

compress = {}

for i in range(len(sorted_num)):
    value = sorted_num[i]
    compress[value] = i

# compress = {-10: 0, -9: 1, 2: 2, 4: 3}

for i in num:
    print(compress[i], end=' ')
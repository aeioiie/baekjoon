N = int(input())
card = set(map(int, input().split())) # set으로 해야 O(1) 시간복잡도로 검색 가능
M = int(input())
num = list(map(int, input().split()))

for i in num:
    if i in card:
        print(1, end=' ')
    else:
        print(0, end=' ')
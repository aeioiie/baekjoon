import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for _ in range(N):
    x = int(input())
    count[x] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)
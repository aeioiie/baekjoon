import sys
input = sys.stdin.readline

N = int(input())
num = []

for i in range(N):
    x = int(input())
    num.append(x)

num.sort()

for i in range(N):
    print(num[i])
A, B = map(int, input().split())
C = int(input())

left = A + B

if left >= 2*C:
    print(left - 2*C)
else:
    print(left)
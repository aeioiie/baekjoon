N = int(input())
rainbow_dance = set()

for i in range(N):
    A, B = input().split()
    if A == "ChongChong" or B == "ChongChong":
        rainbow_dance.add(A)
        rainbow_dance.add(B)
    if A in rainbow_dance or B in rainbow_dance:
        rainbow_dance.add(A)
        rainbow_dance.add(B)

print(len(rainbow_dance))
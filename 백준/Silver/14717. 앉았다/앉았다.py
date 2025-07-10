A, B = map(int, input().split())

def pedigree(a, b):
    if a == b:
        return f"{a}D"
    return f"{(a+b) % 10}K"

def rank(ped):
    if ped[-1] == 'D':
        return int(ped[:-1]) * 100 # 우선순위 높음
    else:
        return int(ped[:-1]) # 우선순위 낮음
    
# print(pedigree(A, B))

cards = [0] + [2] * 10
cards[A] -= 1
cards[B] -= 1

Y = rank(pedigree(A, B))

win = 0
total = 0

for i in range(1, 11):
    for j in range(i, 11):
        # 같은 숫자 2개 뽑는 경우의 수(땡) = nC2 = n * (n-1) // 2
        if i == j:
            if cards[i] >= 2:
                count = cards[i] * (cards[i] - 1) // 2
                O = rank(pedigree(i, j))
                if Y > O:
                    win += count
                total += count
        # 다른 숫자 2개 뽑는 경우의 수(고) = nC1 * mC1 = n * m
        else:
            if cards[i] >= 1 and cards[j] >= 1:
                count = cards[i] * cards[j]
                O = rank(pedigree(i, j))
                if Y > O:
                    win += count
                total += count

print(f"{win / total:.3f}")
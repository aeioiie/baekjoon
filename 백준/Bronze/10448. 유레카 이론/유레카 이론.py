Test = int(input())

def T(n):
    return n * (n+1) // 2

tri = [T(i) for i in range(1, 45)]

for i in range(Test):
    K = int(input())
    found = False

    for i in tri:
        for j in tri:
            for m in tri:
                if i + j + m == K:
                    found = True
                    break
            if found:
                break
        if found:
            break
    print(1 if found else 0)
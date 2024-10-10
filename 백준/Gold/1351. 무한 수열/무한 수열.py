N, P, Q = map(int, input().split())

dic = {0: 1, 1: 2}

def a(i):
    if i in dic:
        return dic[i]
    dic[i] = a(i//P) + a(i//Q)
    return dic[i]
print(a(N))

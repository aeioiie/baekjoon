N = int(input())

def fact(n):
    if n <= 1:
        ans = 1
    else:
        ans = fact(n-1) * n
    
    return ans
    
print(fact(N))
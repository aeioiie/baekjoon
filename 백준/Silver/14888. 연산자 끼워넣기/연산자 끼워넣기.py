N = int(input())
A = list(map(int, input().split()))
cal = list(map(int, input().split())) # cal[0]: +, cal[1]: -, cal[2]: *, cal[3]: //

# 6
# 1 2 3 4 5 6
# 2 1 1 1

# 최댓값: 1 - 2 // 3 + 4 + 5 * 6
# 최솟값: 1 + 2 + 3 // 4 - 5 * 6

max_value = -float('inf')
min_value = float('inf')

def dfs(index, current_value):
    global max_value, min_value

    if index == N:
        max_value = max(max_value, current_value)
        min_value = min(min_value, current_value)
        return
    
    for i in range(4): # 0: +, 1: -, 2: *, 3: //
        if cal[i] > 0:
            cal[i] -= 1

            if i == 0:
                dfs(index+1, current_value + A[index])
            elif i == 1:
                dfs(index+1, current_value - A[index])
            elif i == 2:
                dfs(index+1, current_value * A[index])
            elif i == 3:
                if current_value < 0:
                    dfs(index+1, -(-current_value // A[index]))
                else:
                    dfs(index+1, current_value // A[index])
            
            cal[i] += 1

dfs(1, A[0])

print(max_value)
print(min_value)
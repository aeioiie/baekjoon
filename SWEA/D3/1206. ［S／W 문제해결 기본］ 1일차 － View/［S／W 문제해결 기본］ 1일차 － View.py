case_number = 0

for _ in range(10):
    case_number += 1
    N = int(input())
    height = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N-2):
        current = height[i]
        surroundings = [height[i-2], height[i-1], height[i+1], height[i+2]]
        max_surrounding = max(surroundings)
        
        if current > max_surrounding:
            cnt += current - max_surrounding

    print(f"#{case_number} {cnt}")
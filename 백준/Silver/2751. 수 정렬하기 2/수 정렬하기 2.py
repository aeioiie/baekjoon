import sys
input = sys.stdin.readline

N = int(input().strip())
l = []

# 한 줄씩 입력을 받아 리스트에 추가
for _ in range(N):
    l.append(int(input().strip()))

def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 각 리스트의 요소를 하나씩 비교하여 결과 리스트에 추가
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남아 있는 요소들을 결과에 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 정렬된 리스트 얻기
sorted_l = merge_sort(l)

# 결과 출력
sys.stdout.write("\n".join(map(str, sorted_l)) + "\n")

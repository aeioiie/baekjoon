N = int(input())
data = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

data.sort() # 이진 검색을 위한 전제 조건

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return "1"
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return "0"

for target in targets:
  print(binary_search(data, target, 0, N-1))
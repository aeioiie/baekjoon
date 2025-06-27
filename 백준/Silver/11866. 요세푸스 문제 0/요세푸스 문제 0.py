N, K = map(int, input().split()) # 7, 3
p = list(range(1, N+1))
result = []
index = 0

while p:
    index = (index + K - 1) % len(p) # 제거할 인덱스 = (현재 인덱스 + K - 1) % 현재 리스트 길이
    # 제거된 숫자: 3, 6, 2, 7, 5, 1, 4
    # 제거된 인덱스: 2, 4, 1, 3, 2, 0, 0
    # 원형 순회를 하기 위해서는 전체 길이로 나누어 주어야 함
    # 리스트의 끝을 넘으면 처음으로 돌아간다 == (현재 위치 + 이동할 거리) % 전체 길이

    result.append(p.pop(index))

print("<" + ", ".join(map(str, result)) + ">")
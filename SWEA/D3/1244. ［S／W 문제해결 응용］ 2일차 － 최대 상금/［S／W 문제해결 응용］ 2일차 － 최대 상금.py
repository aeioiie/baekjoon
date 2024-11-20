def dfs(number, depth, max_depth):
    global max_value
    # 종료 조건: 교환 횟수를 모두 소진한 경우
    if depth == max_depth:
        max_value = max(max_value, int("".join(number)))
        return

    # 현재 상태를 기준으로 가능한 모든 교환 수행
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            # 자리 교환
            number[i], number[j] = number[j], number[i]
            # 중복 방지를 위해 현재 상태 저장 후 탐색
            current_state = "".join(number)
            if (current_state, depth + 1) not in visited:
                visited.add((current_state, depth + 1))
                dfs(number, depth + 1, max_depth)
            # 원상복구
            number[i], number[j] = number[j], number[i]


# 테스트 케이스 처리
T = int(input())
for t in range(1, T + 1):
    num, k = input().split()
    k = int(k)
    number = list(num)

    # 전역 변수 초기화
    max_value = 0
    visited = set()

    # DFS 탐색 시작
    dfs(number, 0, k)

    # 결과 출력
    print(f"#{t} {max_value}")

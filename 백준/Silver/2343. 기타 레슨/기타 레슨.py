def min_blu_ray_size(lessons, M):
    left, right = max(lessons), sum(lessons)  # 이분 탐색 범위 설정

    while left < right:
        mid = (left + right) // 2  # 중간 크기 설정
        count, total = 1, 0  # 블루레이 개수, 현재 블루레이에 담긴 길이

        for lesson in lessons:
            if total + lesson > mid:  # 현재 블루레이 용량 초과
                count += 1  # 새로운 블루레이 필요
                total = 0  # 새 블루레이에 강의 담기 시작
            total += lesson  # 현재 블루레이에 강의 추가

        if count <= M:  # 블루레이 개수가 M 이하라면
            right = mid  # 크기를 줄여서 탐색
        else:
            left = mid + 1  # 크기를 늘려서 탐색

    return left  # 최소 블루레이 크기 반환

n, m = map(int, input().split())
lec = list(map(int, input().split()))

print(min_blu_ray_size(lec, m))
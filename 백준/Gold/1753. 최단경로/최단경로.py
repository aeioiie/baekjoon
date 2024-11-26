import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    # 최단 거리 배열 초기화
    distance = [INF] * (V + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))  # (거리, 정점)

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 이미 처리된 적이 있는 거리라면 스킵
        if current_distance > distance[current_node]:
            continue

        # 현재 노드의 모든 인접 노드 확인
        for adjacent, weight in graph[current_node]:
            new_distance = current_distance + weight

            # 최단 거리 갱신
            if new_distance < distance[adjacent]:
                distance[adjacent] = new_distance
                heapq.heappush(queue, (new_distance, adjacent))

    return distance

# 입력 처리
V, E = map(int, input().split())  # 정점과 간선 개수
K = int(input())  # 시작 정점

# 그래프 초기화
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # 방향 그래프

# 다익스트라 알고리즘 실행
distances = dijkstra(K)

# 결과 출력
for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])

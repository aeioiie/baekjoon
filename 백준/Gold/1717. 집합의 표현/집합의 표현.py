# 루트 노드를 찾으면서 경로 압축(Path Compression) 수행
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 집합을 합침
def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        # Rank가 높은 쪽을 루트로 삼음
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # 부모 테이블 초기화
rank = [0] * (n + 1)  # 랭크 테이블 초기화

for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:  # union 연산
        union(parent, rank, a, b)
    elif command == 1:  # find 연산
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")

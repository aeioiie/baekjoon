N, M = map(int, input().split())
not_heard_set = set()
not_seen_set = set()

for i in range(N):
    not_heard = input()
    not_heard_set.add(not_heard)
for i in range(M):
    not_seen = input()
    not_seen_set.add(not_seen)

not_heard_seen = not_heard_set.intersection(not_seen_set)

print(len(not_heard_seen))

for i in sorted(not_heard_seen):
    print(i)
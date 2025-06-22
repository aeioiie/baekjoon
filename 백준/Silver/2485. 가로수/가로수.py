from math import gcd

N = int(input())
trees = []
distances = set()
count = 0

for i in range(N):
    t = int(input())
    trees.append(t)

trees = sorted(trees)

for i in range(N-1):
    d = trees[i+1] - trees[i]
    distances.add(d)

distances = sorted(distances)
min_distance = distances[0]

for d in distances[1:]:
    min_distance = gcd(min_distance, d)

for i in range(N-1):
    if trees[i+1] - trees[i] != min_distance:
        count += ((trees[i+1]-trees[i]) // min_distance) - 1
    else:
        continue

print(count)
from collections import Counter
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
words = []

for i in range(N):
    word = input().strip()
    if len(word) >= M:
        words.append(word)

counter = Counter(words)
words = sorted(set(words), key=lambda x: (-counter[x], -len(x), x))

# print(words)

for word in words:
    print(word)
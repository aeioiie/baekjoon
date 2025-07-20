S = input()
count = [0] * 26

for char in S:
    count[ord(char) - ord('a')] += 1

print(' '.join(map(str, count)))
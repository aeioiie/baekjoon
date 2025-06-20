S = input()
s_diff = set()

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        s_diff.add(S[i:j])

print(len(s_diff))
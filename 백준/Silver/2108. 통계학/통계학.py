import sys
input = sys.stdin.readline

N = int(input())
S = []
M = []

for i in range(N):
    I = int(input())
    S.append(I)

S.sort()

# 산술평균
mean = sum(S) / N
if mean >= 0:
    mean_rounded = int(mean + 0.5)
else:
    mean_rounded = int(mean - 0.5)

# 중앙값
median = S[N//2]

# 최빈값
max_freq = 0
curr_val = S[0]
curr_cnt = 0
modes = []

for i in S:
    if i == curr_val:
        curr_cnt += 1
    else:
        if curr_cnt > max_freq:
            max_freq = curr_cnt
            modes = [curr_val]
        elif curr_cnt == max_freq:
            modes.append(curr_val)
        curr_val = i
        curr_cnt = 1
        
if curr_cnt > max_freq:
    max_freq = curr_cnt
    modes = [curr_val]
elif curr_cnt == max_freq:
    modes.append(curr_val)

modes.sort()

if len(modes) > 1:
    mode = modes[1]
else:
    mode = modes[0]

# 범위
range_val = S[-1] - S[0]

print(mean_rounded)
print(median)
print(mode)
print(range_val)
A, B = map(int, input().split())
C = int(input())

C1 = C // 60 # C를 60으로 나눈 몫
C2 = C % 60 # C를 60으로 나눈 나머지

if (B + C2) >= 60: # B와 C2의 합이 60보다 크거나 같을 때
    B1 = (B + C2) // 60 # B1은 그 합을 60으로 나눈 몫
    B2 = (B + C2) % 60 # B2는 그 합을 60으로 나눈 나머지
    new_A = A + C1 + B1 # 시간에 몫을 더함
    new_B = B2 # 분은 나머지로 설정
else:
    new_A = A + C1 # B와 C2의 합이 60보다 작으면 시간에 몫만 더함
    new_B = B + C2 # 분에는 C2만 더함

# 24시간 넘길 경우 조정
if new_A >= 24:
    new_A -= 24

print(new_A, new_B)
N, M = input().split() # 입력 값을 문자열로 받음

N = N[::-1] # 문자열을 뒤집음
M = M[::-1] # 문자열을 뒤집음

if int(N) > int(M): # 뒤집은 문자열을 정수로 변환 후 비교
  print(int(N))
else:
  print(int(M))
T, S = map(int, input().split())

if 12 <= T <= 16 and S == 0:
    print(320)
elif 12 <= T <= 16 and S == 1:
    print(280)
elif (T < 12 or T > 16) and S == 0:
    print(280)
else:
    print(280)

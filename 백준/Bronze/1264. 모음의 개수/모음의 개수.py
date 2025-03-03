while True:
    cnt = 0
    t = input()

    if t == '#':
        break
    
    for i in t:
        if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            cnt += 1
    
    print(cnt)
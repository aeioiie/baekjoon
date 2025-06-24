import sys

N = int(sys.stdin.readline())
stack = []

def f(s):
    cmd = int(s[0])
    if cmd == 1:
        stack.append(int(s[1])) 
    elif cmd == 2:
        if stack:
            return stack.pop()
        else:
            return -1
    elif cmd == 3:
        return len(stack)
    elif cmd == 4:
        if not stack:
            return 1
        else:
            return 0
    elif cmd == 5:
        if stack:
            return stack[-1]
        else:
            return -1

for i in range(N):
    s = sys.stdin.readline().split()
    result = f(s)

    if result is not None:
        print(result)
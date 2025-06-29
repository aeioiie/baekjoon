from collections import deque
import sys

deq = deque()

def dq(o):
    if o[0] == "1":
        deq.appendleft(o[1])
    elif o[0] == "2":
        deq.append(o[1])
    elif o[0] == "3":
        if deq:
            return deq.popleft()
        else:
            return -1
    elif o[0] == "4":
        if deq:
            return deq.pop()
        else:
            return -1
    elif o[0] == "5":
        return len(deq)
    elif o[0] == "6":
        if not deq:
            return 1
        else:
            return 0
    elif o[0] == "7":
        if deq:
            return deq[0]
        else:
            return -1
    elif o[0] == "8":
        if deq:
            return deq[-1]
        else:
            return -1

N = int(sys.stdin.readline())
for i in range(N):
    o = sys.stdin.readline().split()
    result = dq(o)

    if result is not None:
        print(result)
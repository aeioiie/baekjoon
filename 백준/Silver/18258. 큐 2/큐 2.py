from collections import deque
import sys

q_list = deque()

def q(o):
    if o[0] == "push":
        q_list.append(o[1])
    elif o[0] == "pop":
        if q_list:
            return q_list.popleft()
        else:
            return -1
    elif o[0] == "size":
        return len(q_list)
    elif o[0] == "empty":
        if not q_list:
            return 1
        else:
            return 0
    elif o[0] == "front":
        if q_list:
            return q_list[0]
        else:
            return -1
    elif o[0] == "back":
        if q_list:
            return q_list[-1]
        else:
            return -1

N = int(sys.stdin.readline())

for i in range(N):
    o = sys.stdin.readline().split()
    result = q(o)
    
    if result is not None:
        print(result)
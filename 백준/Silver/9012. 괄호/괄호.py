T = int(input())

for i in range(T):
    p = input()
    stack = []

    def vps(p):
        for char in p:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return "NO"
                stack.pop()

        if not stack:
            return "YES"
        else:
            return "NO"
            
    print(vps(p))
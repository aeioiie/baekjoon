n1 = int(input())
n2 = int(input())

n2_list = list(str(n2))

a = n1 * int(n2_list[2])
b = n1 * int(n2_list[1])
c = n1 * int(n2_list[0])

print(a)
print(b)
print(c)
print(a + b*10 + c*100)
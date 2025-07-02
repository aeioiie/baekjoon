N = int(input())
i = 1
fact = 1

while i <= N:
  fact *= i
  i += 1
  
print(fact)
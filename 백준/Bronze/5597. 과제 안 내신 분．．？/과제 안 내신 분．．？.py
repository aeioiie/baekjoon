students = [i for i in range(1, 31)]

for j in range(28):
  applied = int(input())
  students.remove(applied)

print(min(students))
print(max(students))
a_list = []

for i in range(9):
  a = int(input())
  a_list.append(a)

max_number = max(a_list)
max_index = a_list.index(max_number) + 1 # 인덱스는 0부터 시작하므로 +1을 해줌

print(max_number)
print(max_index)
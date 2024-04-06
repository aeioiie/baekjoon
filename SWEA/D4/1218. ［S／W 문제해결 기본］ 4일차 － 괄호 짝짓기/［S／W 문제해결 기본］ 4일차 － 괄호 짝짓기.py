pare = {'>': '<', ')': '(', '}': '{', ']': '['}

for i in range(10):
  n = int(input())
  data = list(input())
  s = []
  ans = 0
  c = True

  while data:
    k = data.pop(0)
    if k in pare.values():
      s.append(k)
    elif s and s[-1] == pare[k]:
      s.pop()
    else:
      c = False
      break

  if not s and c:
    ans = 1
  print(f"#{i+1} {ans}")
w = input()
is_palindrome = True

for i in range(len(w) // 2):
  if w[i] != w[len(w)-i-1]:
    is_palindrome = False
    break

if is_palindrome:
  print("1")
else:
  print("0")
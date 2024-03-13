S = input()
alphabet_list = ["a", "b", "c", "d", "e", "f",
                 "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r",
                 "s", "t", "u", "v", "w", "x",
                 "y", "z"]

for alphabet in alphabet_list:
  if alphabet in S:
    print(S.index(alphabet), end=" ")
  else:
    print(-1, end=" ")
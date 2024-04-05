w = input()
c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in c:
  w = w.replace(i, "0")

print(len(w))
dwarfs = []

for i in range(9):
    height = int(input())
    dwarfs.append(height)

total = sum(dwarfs)

for i in range(9):
    for j in range(i+1, 9):
        if total - dwarfs[i] - dwarfs[j] == 100:
            dwarfs.pop(max(i, j))
            dwarfs.pop(min(i, j))
            break
    else:
        continue
    break
    

if len(dwarfs) == 7:
    dwarfs.sort()
    for dwarf in dwarfs:
        print(dwarf)
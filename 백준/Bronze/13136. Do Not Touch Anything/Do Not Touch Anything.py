import math

R, C, N = map(int, input().split())

rows = math.ceil(R/N)
cols = math.ceil(C/N)

print(rows*cols)
from itertools import product

A = [1, 2]
B = [3, 4]

ans = product(A, B)

print(*ans)
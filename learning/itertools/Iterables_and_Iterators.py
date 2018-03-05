from itertools import combinations

N = 4
L = ['a', 'a', 'b', 'c']
K = 2

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print(C)
print(list(F))
print("{0:.3}".format(len(list(F)) / len(C)))

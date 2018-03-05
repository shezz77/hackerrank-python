from itertools import permutations

s, k = input().split()

print(list(permutations(['1', '2', '3'], 2)))

print(*[''.join(i) for i in permutations(sorted(s), int(k))], sep='\n')

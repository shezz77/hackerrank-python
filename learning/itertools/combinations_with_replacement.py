from itertools import combinations_with_replacement

print(list(combinations_with_replacement('abcd', 2)))

items, k = input().split()

for i in combinations_with_replacement(sorted(items), int(k)):
    print(''.join(i))
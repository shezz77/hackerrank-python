from itertools import combinations


print(list(combinations('1234567', 2)))

items, k = input().split()

for i in range(1, int(k)+1):
    for j in combinations(sorted(items), i):
        print(''.join(j))

# print(list(combinations(items, k)))

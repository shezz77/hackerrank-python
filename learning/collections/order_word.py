from collections import OrderedDict

d = OrderedDict()

for _ in range(int(input())):
    key = input()
    d[key] = d.get(key, 0) + 1

print(len(d.keys()))
print(*d.values())

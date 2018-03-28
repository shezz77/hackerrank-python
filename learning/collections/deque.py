from collections import deque

d = deque()

for _ in range(int(input())):
    values = input().split()

    getattr(d, values[0])(*[values[1]] if len(values) > 1 else [])

print(*[item for item in d])
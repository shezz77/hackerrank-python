s = set(map(int, "1 2 3 4 5 6 7 8 9".split()))

for _ in range(int(input())):
    method, *args = input().split()
    getattr(s, method)(*map(int, args))

print(s)

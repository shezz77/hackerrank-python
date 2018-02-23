N = int(input())

lists = []

for x in range(N):
    s = input().split()
    if hasattr(lists, s[0]):
        getattr(lists, s[0])(*map(int, s[1:]))
    else:
        print(lists)

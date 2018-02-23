n = int(input())
scores = list(map(int, input().split()))

topper = max(scores)

while max(scores) == topper:
    scores.remove(max(scores))

print(scores)
print(max(scores))
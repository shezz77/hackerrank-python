from collections import Counter

num_shoes = int(input())
shoes = Counter(map(int, input().split()))
num_customer = int(input())

income = 0

for i in range(num_customer):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] += 1

print(income)
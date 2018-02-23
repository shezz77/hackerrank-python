from functools import reduce

items = [1, 2, 3, 4]

result = reduce((lambda x, y: x*y), items)

print(result)
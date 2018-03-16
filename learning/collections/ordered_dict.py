from collections import OrderedDict

ordinary_dictionary = OrderedDict()
ordinary_dictionary['a'] = 1
ordinary_dictionary['b'] = 2
ordinary_dictionary['c'] = 3
ordinary_dictionary['d'] = 4
ordinary_dictionary['e'] = 5

print(ordinary_dictionary)

d = OrderedDict()

n = 9

for _ in range(n):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)

for item, quantity in d.items():
    print(item, quantity)

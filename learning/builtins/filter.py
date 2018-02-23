item_list = list(range(-10, 12))

result = list(filter((lambda x: x > 0), item_list))

print(result)

a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 5, 6, 7, 8]

result2 = list(filter(lambda x: x in a, b))
result3 = [x for x in a if x in b]

print(result2)
print(result3)
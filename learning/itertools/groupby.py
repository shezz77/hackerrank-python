# compress strings
from itertools import groupby

items = '1119999992222333333334445566666767888888'

# print(*[(len(list(items)), int('4')) for k, c in groupby(items)])
print(*[(len(list(c)), int(k)) for k, c in groupby(items)])
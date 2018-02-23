import textwrap
string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = 4

print(string)

for i in range(0, len(string)+1, w):
    print(string[i:w+i])


lis = " ".join(textwrap.wrap(string, w))
print(textwrap.fill(lis, w))

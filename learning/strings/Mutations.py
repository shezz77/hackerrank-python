string = "abracadabra"

string_list = list(string)

print(string_list)

string_list[5] = 'k'

print(string_list)

result = ''.join(string_list)

print(result)

result2 = string[:5] + 'k' + string[6:]

print(result2)
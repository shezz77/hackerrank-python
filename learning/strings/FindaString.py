string = "ABCDCDCDCDC"
sub_string = "CDC"

print(sum([1 for i in range(len(string) - len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string]))
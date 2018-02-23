full_name = "shehzad aslam"

split = full_name.split()

print(full_name.title())
print(split)

for x in split:
    full_name = full_name.replace(x, x.capitalize())


print(full_name)
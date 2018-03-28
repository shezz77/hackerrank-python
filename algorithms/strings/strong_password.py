n = 11
val = '#HackerRank'


# def minimum_number(n, password):
#     count = 0
#     if any(i.isdigit() for i in password)==False:
#         count+=1
#     if any(i.islower() for i in password)==False:
#         count+=1
#     if any(i.isupper() for i in password)==False:
#         count+=1
#     if any(i in '!@#$%^&*()-+' for i in password)==False:
#         count+=1
#     return max(count, 6-n)


# print(minimum_number(n, val))


count = 0

if not any(i.isdigit() for i in val):
    count += 1
if not any(i.islower() for i in val):
    count += 1
if not any(i.isupper() for i in val):
    count += 1
if not any(i in '!@#$%^&*()-+' for i in val):
    count += 1

print(max(count, 6-n))




mark_sheet = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# for _ in range(0, int(input())):
#     mark_sheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in mark_sheet])))[1]

# print(second_highest)

print('\n'.join([a for a, b in sorted(mark_sheet) if b == second_highest]))
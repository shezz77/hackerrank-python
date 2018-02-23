a = set("2 4 5 9".split())
b = set("2 4 11 12".split())

print("\n".join(sorted(a.symmetric_difference(b), key=int)))
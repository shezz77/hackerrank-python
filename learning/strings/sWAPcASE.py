s = "HackerRank.com presents \"Pythonist 2\"."

print(''.join([i.lower() if i.isupper() else i.upper() for i in s]))
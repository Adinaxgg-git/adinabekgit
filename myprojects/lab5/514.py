import re

n = input()
pattern = re.compile(r"^[0-9]+$")
if pattern.fullmatch(n):
    print("Match")
else:
    print("No match")
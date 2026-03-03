import re

n = input()
matches = re.findall(r"\d{2,}", n)
print(" ".join(matches))
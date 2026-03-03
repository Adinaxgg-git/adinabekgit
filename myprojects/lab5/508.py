import re

string = input()
pattern = input()

parts = re.split(pattern, string)

print(",".join(parts))
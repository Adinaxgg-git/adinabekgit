import re

string = input()
pattern = input()

matches = re.findall(pattern, string)
print(len(matches))
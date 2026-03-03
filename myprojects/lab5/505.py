import re

n=input()
if re.match(r"^[A-Za-z].*[0-9]$",n):
    print("Yes")
else:
    print("No")
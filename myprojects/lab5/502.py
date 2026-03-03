import re

text=input()
substring=input()

if re.search(substring,text):
    print("Yes")
else:
    print("No")
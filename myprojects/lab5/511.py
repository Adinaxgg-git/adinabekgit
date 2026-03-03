import re
n=input()
count=re.findall(r"[A-Z]",n)
print(len(count))
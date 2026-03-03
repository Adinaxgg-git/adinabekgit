import re
n=input()
if re.search(r"cat|dog",n):
    print("Yes")
else:
    print("No")
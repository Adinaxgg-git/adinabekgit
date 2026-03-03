import re
string=input()
substring=input()
replacement_string=input()

string = re.sub(substring, replacement_string, string)
print(string)
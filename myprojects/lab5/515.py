import re

def double_digit(match):
    return match.group() * 2

text = input()
result = re.sub(r'\d', double_digit, text)
print(result)
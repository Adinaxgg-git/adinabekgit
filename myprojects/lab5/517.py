import re

text = input()

pattern = r"\b\d{2}/\d{2}/\d{4}\b"
dates = re.findall(pattern, text)

print(len(dates))
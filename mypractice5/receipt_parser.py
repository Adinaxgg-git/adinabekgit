# receipt_parser.py
import re

# Открываем файл с чеком
with open("raw.txt", "r") as f:
    data = f.read()

# Находим все строки с товарами и ценой
items = re.findall(r"(\w[\w\s]+)\s+(\d+\.\d+)", data)

print("Parsed Items:")
for item, price in items:
    print(f"{item.strip()}: ${price}")
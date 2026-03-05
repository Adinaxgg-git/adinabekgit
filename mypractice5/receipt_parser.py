import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

prices = re.findall(r'\d{1,3}(?: \d{3})*,\d{2}', text)

products = re.findall(r'\d+\.\s*(.*?)\n\d', text, re.DOTALL)
products = [p.strip().replace('\n',' ') for p in products]

total_match = re.search(r'ИТОГО:\s*([\d\s,]+)', text)
total_amount = total_match.group(1).strip() if total_match else None


datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})', text)
datetime = datetime_match.group(1) if datetime_match else None

payment_match = re.search(r'Банковская карта|Наличные', text)
payment_method = payment_match.group(0) if payment_match else None

receipt_data = {
    "products": [{"name": name, "price": price} for name, price in zip(products, prices)],
    "total_amount": total_amount,
    "datetime": datetime,
    "payment_method": payment_method
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=2))
import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()


#прайс 
price_pattern = r"x\s([\d\s]+,\d{2})"
prices_raw = re.findall(price_pattern, text)

prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices_raw]

#название 
product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, text)

total = sum(prices)

#время и дата 

datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime_match = re.search(datetime_pattern, text)

date = None
time = None

if datetime_match:
    date_time = datetime_match.group()
    date, time = date_time.split()

#метод оплаты

payment_pattern = r"Банковская карта|Наличные"
payment_match = re.search(payment_pattern, text)

payment_method = payment_match.group() if payment_match else "Unknown"


result = {
    "products": products,
    "prices": prices,
    "total_calculated": total,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(result, indent=4, ensure_ascii=False))
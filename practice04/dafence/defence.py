import json
import os

base = os.path.dirname(__file__)
path = os.path.join(base, "cars.json")

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

if isinstance(data, list):
    items = data
elif isinstance(data, dict) and "cars" in data and isinstance(data["cars"], list):
    items = data["cars"]
elif isinstance(data, dict):
    items = [{"model": k, "price": v} for k, v in data.items()]
else:
    items = []

car_map = {}
for it in items:
    if isinstance(it, dict) and "model" in it and "price" in it:
        car_map[str(it["model"]).lower()] = {"model": str(it["model"]), "price": float(it["price"])}

chosen = []
total = 0.0

while True:
    s = input().strip()
    if s.lower() == "done":
        break

    key = s.lower()
    if key in car_map:
        car = car_map[key]
        chosen.append(car["model"])
        total += car["price"]
        print(f"Yes: {car['model']} {car['price']}")
    else:
        print("No")

print("Chosen:", ", ".join(chosen) if chosen else "None")
print("Total:", total)
import json

#1 JSON Syntax
s = '{"name":"Bekaly","age":18,"is_student":true,"skills":["python","git"]}'
print(s)

#2 Parsing JSON (json.loads())
data = json.loads('{"city":"Almaty","temp":-5}')
print(data["city"], data["temp"])

#3 Converting Python to JSON (json.dumps())
person = {"name": "Bekaly", "age": 18, "active": True}
print(json.dumps(person))

#4 Writing JSON Files
obj = {"id": 1, "items": ["a", "b", "c"]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(obj, f)

#5 Reading JSON Files
with open("data.json", "r", encoding="utf-8") as f:
    obj2 = json.load(f)
print(obj2)

#6
with open("sample-data.json", "r", encoding="utf-8") as f:
    sample = json.load(f)
print(sample[0] if isinstance(sample, list) and sample else sample)
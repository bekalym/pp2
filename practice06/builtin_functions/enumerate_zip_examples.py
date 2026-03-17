names = ["Ali", "Aruzhan", "Bek"]
scores = [90, 85, 88]

for i, name in enumerate(names, start=1):
    print(i, name)

for name, score in zip(names, scores):
    print(name, score)

x = "123"
y = int(x)

print(type(x), x)
print(type(y), y)
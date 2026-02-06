#1
i = 0
while True:
    print(i)
    if i == 3:
        break
    i += 1

#2
while True:
    s = input("Введите слово: ")
    if s == "stop":
        break

#3
nums = [4, 7, 2, 9]
i = 0

while i < len(nums):
    if nums[i] == 2:
        print("Found!")
        break
    i += 1
#4
password = "1234"

while True:
    p = input("Пароль: ")
    if p == password:
        print("OK")
        break
    print("Wrong")

#5
total = 0
i = 1

while True:
    total += i
    if total > 10:
        break
    i += 1

print(total)


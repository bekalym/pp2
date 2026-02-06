#1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#2
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

#3
nums = [3, -1, 5, -2, 7]
i = 0

while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1

#4
while True:
    s = input("Введите что-то: ")
    if s == "":
        continue
    print("Вы ввели:", s)
    break

#5
nums = [10, 0, 5, 0, 2]
i = 0

while i < len(nums):
    if nums[i] == 0:
        i += 1
        continue
    print(10 / nums[i])
    i += 1

#1
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#2
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

#3
nums = [3, -1, 5, -2, 7]
for x in nums:
    if x < 0:
        continue
    print(x)

#4
text = "a b  c"
for ch in text:
    if ch == " ":
        continue
    print(ch)

#5
nums = [10, 0, 5, 0, 2]
for x in nums:
    if x == 0:
        continue
    print(10 / x)

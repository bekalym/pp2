#1
for i in range(1, 10):
    if i == 4:
        break
    print(i)

#2
nums = [5, 8, 2, 9]
for x in nums:
    if x == 2:
        print("Found")
        break

#3for _ in range(100):
    s = input("Введите: ")
    if s == "stop":
        break
    
#4
text = "hello world"
for ch in text:
    if ch == " ":
        break
    print(ch)

#5
n = 21
for d in range(2, n):
    if n % d == 0:
        print("Divisor:", d)
        break


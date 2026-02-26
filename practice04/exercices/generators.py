#1
def squares_upto(n):
    for i in range(n + 1):
        yield i * i

print("Task 1:", list(squares_upto(10)))


#2
def evens_upto(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

print("Task 2:", ",".join(map(str, evens_upto(20))))


#3
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("Task 3:", list(div_by_3_and_4(100)))


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

print("Task 4:")
for x in squares(3, 8):
    print(x)


#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

print("Task 5:", list(countdown(10)))
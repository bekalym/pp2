#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#2
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#3
all_numbers = list(filter(lambda x: x % 2 == 0 or x % 2 != 0, numbers))
print(all_numbers)

#4
filtered_numbers = list(filter(lambda x: x > 4, numbers))
print(filtered_numbers)

#5
filtered_numbers = list(filter(lambda x: x < 4, numbers))
print(filtered_numbers)


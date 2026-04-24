#1 вызывает функцию и печатает сообщение
def my_function():
  print("Hello from a function")

my_function()

#2 вызывает функцию три раза
def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

#3 переводит 77°F в °C и выводит результат
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

#4
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77)) # преобразует и печатает для 77°F
print(fahrenheit_to_celsius(88)) # преобразует и печатает для 88°F
print(fahrenheit_to_celsius(99)) # преобразует и печатает для 99°F

#5 возвращает строку из функции
def get_greeting():
    return "hello from a function"
message = get_greeting()
print(message)
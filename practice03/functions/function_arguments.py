#1 функция принимает аргумент и печатает его с добавлением "Refsnes"
def my_function(fname):
    print(fname + " Refsnes")

my_function("John")
my_function("Jane")
my_function("Doe")

#2 
def my_function(fname,lname):
    print(fname + " " + lname)

my_function("hello","beka")
my_function("my","class")

#3
def my_function(name = "friend"):
    print("hello" ,name)

my_function("beka")
my_function("damir")
my_function("shadik")
my_function()
my_function("era")

#4
def my_function(name,animal):
    print("i have a", animal)
    print("my",animal + "'s name is", name)

my_function(name = "rex", animal = "dog")
my_function(name = "prepre", animal = "flamingo")

#5
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
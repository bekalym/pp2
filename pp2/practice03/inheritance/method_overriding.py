#1
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Cat(Animal):
    def sound(self):
        print("Cat says: meow")


a = Animal()
c = Cat()
a.sound()
c.sound()
print()

#2
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


r = Rectangle(5, 3)
print(r.area())
print()


#3
class Person:
    def greet(self):
        print("Hello!")


class Student(Person):
    def greet(self):
        print("Hello, I am a student!")


p = Person()
s = Student()
p.greet()
s.greet()
print()


#4
class Vehicle:
    def move(self):
        print("Vehicle moves")


class Car(Vehicle):
    def move(self):
        print("Car drives")


class Bike(Vehicle):
    def move(self):
        print("Bike rides")


v = Vehicle()
car = Car()
bike = Bike()
v.move()
car.move()
bike.move()
print()


#5
class Logger:
    def log(self, message):
        print("LOG:", message)


class TimeLogger(Logger):
    def log(self, message):
        print("TIME LOG:", message)


l = Logger()
tl = TimeLogger()
l.log("Started")
tl.log("Started")

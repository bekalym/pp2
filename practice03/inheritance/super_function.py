#1
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog says: woof")


d = Dog()
d.sound()
print()


#2
class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def info(self):
        super().info()
        print("Group:", self.group)


s = Student("Bekaly", "SE-2401")
s.info()
print()


#3
class Calculator:
    def add(self, a, b):
        return a + b


class AdvancedCalculator(Calculator):
    def add(self, a, b):
        result = super().add(a, b)
        return result + 10


calc = AdvancedCalculator()
print(calc.add(5, 3))
print()


#4
class Logger:
    def log(self, text):
        print("[LOG]:", text)


class FileLogger(Logger):
    def log(self, text):
        super().log(text)
        self.save(text)

    def save(self, text):
        print("Saving to file:", text)


fl = FileLogger()
fl.log("Hello")
print()


#5
class Base:
    def greet(self):
        print("Hello from Base")


class Child(Base):
    def greet(self):
        super().greet()
        print("Hello from Child")


c = Child()
c.greet()

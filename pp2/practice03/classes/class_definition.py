#1 Чтобы создать класс, используйте ключевое слово class
class MyClass:
  x = 5

print(MyClass)

#2 Создайте объект класса, создав экземпляр класса, и присвойте его переменной
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

#3 Создайте класс с инициализатором 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)

#4 Создайте несколько экземпляров класса
class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#5 Измените значение свойства класса для всех экземпляров класса
class MyClass:
  x = 10

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
#1 Переменная класса (общая) и переменная объекта (индивидуальная)

class Student:
    university = "AITU" 

    def __init__(self, name):
        self.name = name  


s1 = Student("Bekaly")
s2 = Student("Aruzhan")

print("#1")
print(s1.name, s1.university)  
print(s2.name, s2.university)
print()


#2 Если поменять переменную класса через класс — изменится для всех объектов
class Phone:
    brand = "Apple"  

    def __init__(self, model):
        self.model = model  


p1 = Phone("iPhone 13")
p2 = Phone("iPhone 15")

print("#2")
print(p1.brand, p2.brand)  

Phone.brand = "Samsung"  
print(p1.brand, p2.brand)  
print()


#3 Переменная объекта может "затенить" переменную класса (shadowing)
class Car:
    wheels = 4  

    def __init__(self, name):
        self.name = name


c1 = Car("Toyota")
c2 = Car("BMW")

print("#3")
print(c1.wheels, c2.wheels)  
c1.wheels = 6  
print(c1.wheels, c2.wheels)  

print("Car.wheels:", Car.wheels)    
print()


#4 Переменная класса как счётчик (полезный кейс)
class User:
    count = 0 

    def __init__(self, username):
        self.username = username
        User.count += 1  

u1 = User("user1")
u2 = User("user2")
u3 = User("user3")

print("#4")
print("Сколько создано пользователей:", User.count)  # 3
print()

#5 Частая ошибка: изменяемый объект (list) как переменная класса
class TeamBad:
    members = [] 
    def add_member(self, name):
        self.members.append(name)  


t1 = TeamBad()
t2 = TeamBad()

t1.add_member("Ali")
t2.add_member("Dana")

print("#5 (плохой пример)")
print("t1:", t1.members) 
print("t2:", t2.members)  
print()

# Правильный вариант: список должен быть переменной объекта
class TeamGood:
    def __init__(self):
        self.members = []   

    def add_member(self, name):
        self.members.append(name)


tg1 = TeamGood()
tg2 = TeamGood()

tg1.add_member("Ali")
tg2.add_member("Dana")

print("#5 (хороший пример)")
print("tg1:", tg1.members)  
print("tg2:", tg2.members)  

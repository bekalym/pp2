#1
class A:
    def show_a(self):
        print("A")


class B:
    def show_b(self):
        print("B")


class C(A, B):
    pass


c = C()
c.show_a()
c.show_b()
print()


#2
class Flyable:
    def fly(self):
        print("I can fly")


class Swimable:
    def swim(self):
        print("I can swim")


class Duck(Flyable, Swimable):
    pass


d = Duck()
d.fly()
d.swim()
print()


#3
class Camera:
    def feature(self):
        print("Camera: take photos")


class Phone:
    def feature(self):
        print("Phone: make calls")


class SmartDevice(Camera, Phone):
    def feature(self):
        super().feature()
        print("SmartDevice: use apps")


sd = SmartDevice()
sd.feature()
print()


#4
class Logger:
    def log(self, text):
        print("LOG:", text)


class Notifier:
    def notify(self, text):
        print("NOTIFY:", text)


class App(Logger, Notifier):
    def run(self):
        self.log("App started")
        self.notify("Hello user")


app = App()
app.run()
print()

#5 
class X:
    def who(self):
        print("X")


class Y(X):
    def who(self):
        print("Y")
        super().who()


class Z(X):
    def who(self):
        print("Z")
        super().who()


class M(Y, Z):
    def who(self):
        print("M")
        super().who()


m = M()
m.who()

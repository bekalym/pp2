#1 Iterators: iter() and next()

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#2 Loop through an Iterator

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#

mystr = "banana"

for x in mystr:
  print(x)

#3 Create an Iterator

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#4 Generators: yield keyword

def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)

#5 Creating Generator Functions
def fun():
    yield 1            
    yield 2            
    yield 3            
 
for val in fun(): 
    print(val)

#6 Generator Expressions
sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)


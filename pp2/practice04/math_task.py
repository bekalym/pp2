#1 Built-in Math Functions (min, max, abs, round, pow)
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#

x = abs(-7.25)

print(x)

#

x = pow(4, 3)

print(x)

#2 math Module Functions (sqrt, ceil, floor, sin, cos, pi, e)

import math

print(math.sqrt(64))

#

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)
print(y)

#

import math

x = math.pi

print(x)

#

import math

print(math.sin(math.pi / 2))
print(math.cos(0))
print(math.e)
print(math.exp(1))

#3 random Module (random, randint, choice, shuffle)

import random

print(random.random())
print(random.randint(1, 10))
print(random.choice(["apple", "banana", "cherry"]))

a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)
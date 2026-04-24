import math

# Task 1
degree = 15
radian = degree * (math.pi / 180)
print("Input degree:", degree)
print("Output radian:", radian)
print()

# Task 2
h = 5
a = 5
b = 6
area_trapezoid = ((a + b) / 2) * h
print("Height:", h)
print("Base, first value:", a)
print("Base, second value:", b)
print("Expected Output:", area_trapezoid)
print()

# Task 3
n_sides = 4
side_len = 25
area_polygon = (n_sides * (side_len ** 2)) / (4 * math.tan(math.pi / n_sides))
print("Input number of sides:", n_sides)
print("Input the length of a side:", side_len)
print("The area of the polygon is:", area_polygon)
print()

# Task 4
base = 5
height = 6
area_parallelogram = base * height
print("Length of base:", base)
print("Height of parallelogram:", height)
print("Expected Output:", float(area_parallelogram))
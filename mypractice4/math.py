# math.py
import math

# 1. Convert degree to radian
degree = 15
radian = math.radians(degree)
print("Radian:", radian)

# 2. Area of a trapezoid
height = 5
base1 = 5
base2 = 6
area_trapezoid = (base1 + base2) * height / 2
print("Area of trapezoid:", area_trapezoid)

# 3. Area of regular polygon
n_sides = 4
side_length = 25
area_polygon = side_length ** 2  # For square
print("Area of polygon:", area_polygon)

# 4. Area of parallelogram
base = 5
height_parallelogram = 6
area_parallelogram = base * height_parallelogram
print("Area of parallelogram:", area_parallelogram)
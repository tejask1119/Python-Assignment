### Find the area and circumference of circle.

import math

r = float(input("Enter radius: "))

area = math.pi * (r ** 2)
circumference = 2 * math.pi * r

print("Area of circle:", area)
print("Circumference of circle:", circumference)
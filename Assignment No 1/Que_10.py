### Write a program to calculate area of an equilateral triangle.

import math

side = float(input("Enter side: "))
area = (math.sqrt(3) / 4) * (side ** 2)
print("Area of equilateral triangle:", area)

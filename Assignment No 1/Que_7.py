### Program to Find the Roots of a Quadratic Equation :

import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b ** 2 - 4 * a * c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)

    print("Root 1:", root1)
    print("Root 2:", root2)

elif d == 0:
    root = -b / (2 * a)

    print("Both roots are equal:", root)

else:
    print("No real roots")
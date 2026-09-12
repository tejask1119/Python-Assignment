###  WAP to calculate area of triangle and rectangle:

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

triangle_area = (base * height) / 2

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

rectangle_area = length * breadth

print("Area of triangle:", triangle_area)
print("Area of rectangle:", rectangle_area)
## Write a program to enter P, T, R and calculate simple Interest.

p = float(input("Enter Principal: "))
t = float(input("Enter Time: "))
r = float(input("Enter Rate: "))

si = (p * t * r) / 100

print("Simple Interest:", si)

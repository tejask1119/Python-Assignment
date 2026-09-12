## Write a program to enter P, T, R and calculate Compound Interest.

p = float(input("Enter Principal: "))
t = float(input("Enter Time: "))
r = float(input("Enter Rate: "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest:", ci)
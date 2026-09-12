### Write a program to swap two numbers using third variable:

a = int(input("Enter A: "))
b = int(input("Enter B: "))

c = a
a = b
b = c

print("After swapping:")
print("B:", b)
print("A:", a)

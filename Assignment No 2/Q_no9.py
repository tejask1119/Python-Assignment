### Write a program to swap two numbers without using third variable :

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("First number:", a)
print("Second number:", b)
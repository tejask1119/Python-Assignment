### Find the sum of three-digit number :

number = int(input("Enter a three-digit number: "))

digit1 = number % 10
number = number // 10

digit2 = number % 10
number = number // 10

digit3 = number

sum_of_digits = digit1 + digit2 + digit3

print("Sum of digits:", sum_of_digits)

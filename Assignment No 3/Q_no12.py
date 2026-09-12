##  Write a program to check if given 3 digit number is a palindrome or not:

number = int(input("Enter a three-digit number: "))

original = number

digit1 = number % 10
number = number // 10

digit2 = number % 10
number = number // 10

digit3 = number

reverse = (digit1 * 100) + (digit2 * 10) + digit3

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
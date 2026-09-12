### Write a program to reverse three-digit number:

number = int(input("Enter a  number: "))

digit1 = number % 10
number = number // 10

digit2 = number % 10
number = number // 10

digit3 = number

reverse = (digit1 * 100) + (digit2 * 10) + digit3

print("Reverse number:", reverse)
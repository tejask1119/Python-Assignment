## 11. WAP to check if given number Strong Number :

number = int(input("Enter a number: "))

original = number
sum_of_factorials = 0

while number > 0:

    digit = number % 10

    factorial = 1

    for i in range(1, digit + 1):
        factorial = factorial * i

    sum_of_factorials = sum_of_factorials + factorial

    number = number // 10

if sum_of_factorials == original:
    print("Strong Number")
else:
    print("Not a Strong Number")
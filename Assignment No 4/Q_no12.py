## 12. Write a program to check if given number is Armstrong number or not.

number = int(input("Enter a number: "))

original = number

temp = number
count = 0

while temp > 0:
    temp = temp // 10
    count = count + 1

temp = number
armstrong_sum = 0

while temp > 0:
    digit = temp % 10

    armstrong_sum = armstrong_sum + (digit ** count)

    temp = temp // 10

if armstrong_sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
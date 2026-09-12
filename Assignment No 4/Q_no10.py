## 10. WAP to check if given number is Perfect Number :

number = int(input("Enter a number: "))

sum_of_divisors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_divisors = sum_of_divisors + i

if sum_of_divisors == number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
## 7. WAP to print all integers upto n that aren’t divisible by 2 and 3:

n = int(input("Enter n: "))

for number in range(1, n + 1):
    if number % 2 != 0 and number % 3 != 0:
        print(number)
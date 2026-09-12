## 2. WAP to print all odd numbers until n:

n = int(input("Enter n: "))

for number in range(1, n + 1):
    if number % 2 != 0:
        print(number)
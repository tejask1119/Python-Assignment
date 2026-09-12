## 3. WAP to print sum of series upto n:

n = int(input("Enter n: "))

sum = 0

for number in range(1, n + 1):
    sum = sum + number

print("Sum:", sum)
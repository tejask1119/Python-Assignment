## 5. WAP to print Fibonacci series upto n:

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)

    next_number = a + b
    a = b
    b = next_number
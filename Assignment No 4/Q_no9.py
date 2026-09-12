## 9. WAP to print all numbers in a range divisible by a given number:

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
divisor = int(input("Enter the number to divide by: "))

for number in range(start, end + 1):
    if number % divisor == 0:
        print(number)
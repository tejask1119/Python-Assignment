## 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range:

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for number in range(start, end + 1):
    if number % 7 == 0 and number % 5 == 0:
        print(number)
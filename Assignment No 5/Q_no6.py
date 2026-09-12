## Write a program to print first n prime numbers :

n = int(input("Enter how many prime numbers you want: "))

count = 0
number = 2

while count < n:

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
        count = count + 1

    number = number + 1
    
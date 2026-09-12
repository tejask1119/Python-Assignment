## Write a program to print prime numbers between 1 to 100 :

for number in range(2, 101):

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
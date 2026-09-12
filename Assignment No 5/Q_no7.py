# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

n = int(input("Enter n: "))

total = 0

for number in range(1, n + 1):

    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    total = total + factorial

print("Sum of factorial series:", total)
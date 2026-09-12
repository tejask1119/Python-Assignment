## WAP to print Armstrong number within a given range :

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for number in range(start, end + 1):

    original = number

    # Count digits
    temp = number
    count = 0

    while temp > 0:
        temp = temp // 10
        count = count + 1

    # Calculate Armstrong sum
    temp = number
    armstrong_sum = 0

    while temp > 0:
        digit = temp % 10

        armstrong_sum = armstrong_sum + (digit ** count)

        temp = temp // 10

    # Check
    if armstrong_sum == original:
        print(number)
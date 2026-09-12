## 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

number_of_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter per ticket cost: "))

total_amount = 0

for i in range(1, number_of_passengers + 1):

    age = int(input("Enter age of passenger: "))

    if age < 12:
        discount = (ticket_cost * 30) / 100
        final_amount = ticket_cost - discount

    elif age > 59:
        discount = (ticket_cost * 50) / 100
        final_amount = ticket_cost - discount

    else:
        final_amount = ticket_cost

    total_amount = total_amount + final_amount

print("Total ticket amount:", total_amount)
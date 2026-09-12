## Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age = int(input("Enter age of person: "))
ticket_amount = float(input("Enter ticket amount: "))

if age < 12:
        discount = (ticket_amount * 30) / 100
        final_amount = ticket_amount - discount

elif age > 59:
        discount = (ticket_amount * 50) / 100
        final_amount = ticket_amount - discount

else:
        final_amount = ticket_amount

total_amount = final_amount

print("Total ticket amount:", total_amount)
### WAP to calculate selling price of book based on cost price and discount:

cost_price = float(input("Enter cost price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = (cost_price * discount) / 100

selling_price = cost_price - discount_amount

print("Discount Amount:", discount_amount)
print("Selling Price:", selling_price)
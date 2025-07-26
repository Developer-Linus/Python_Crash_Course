sandwich_orders = ["Club Sandwich", "Pastrami", "Grilled Cheese",
                   "BLT", "Pastrami", "Philly Cheesesteak", "Chicken Shawarma Wrap", "Pastrami"]

count = 0
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
    count += 1
print("The number of Pastrami's removed is: " + str(count))
print(sandwich_orders)

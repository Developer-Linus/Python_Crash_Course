sandwich_orders = ["Club Sandwich", "Grilled Cheese",
                   "BLT", "Philly Cheesesteak", "Chicken Shawarma Wrap"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print("I made your " + current_sandwich + " sandwich.")

print("\nThe sandwiches that have been made are: ")
for sandwich in finished_sandwiches:
    print(sandwich)

requested_toppings = ["mushroom", "pepperoni"]

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("Finished preparing your pizza.")
else:
    print('Are you sure you want a plain pizza?')

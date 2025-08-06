def make_pizza(size, *toppings):
    """
    Summarize the type of pizza we are to make.
    """
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, "pepperoni")
make_pizza(22, "mushroom", "green peppers", "cheese")

places = {}

# Set flag to keep polling users active
polling_active = True
while polling_active:
    name = input("What is your first name? ").title()
    place = input(
        "If you could visit one place in the world, where would you go? ")

    places[name] = place
    program_stop = input("Enter 'exit' to pause the program from running.")
    if program_stop == "exit":
        polling_active = False
print("\n_______Poll Results_________")
for name, place in places.items():
    print(name + ' would like to go ' + place + " for a vacation.")

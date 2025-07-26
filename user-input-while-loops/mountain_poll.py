responses = {}
# Set a flag that will keep the program running
active = True
while active:
    name = input(
        "Please give us your first name. Your first name make us to associate your response to you and give personalized feedback ").title()
    response = input("Which mountain would you like to climb some day? ")

    responses[name] = response

    repeat = input(
        'Would you like to allow next person to take the poll? Please answer yes or no. ').lower()
    if repeat == "no":
        active = False

# Printing poll results
print("\n____Poll Results____")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

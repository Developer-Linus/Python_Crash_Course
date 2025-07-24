prompt = ("\nWelcome to our movie shop ticketing system.")
prompt += ("\nPlease enter your age as a whole number (e.g, 3, 16, 18): ")

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        age = int(message)
        if age <= 3:
            print("You ticket to watch movie is FREE")
        elif age <= 12:
            print("The cost of your ticket is $10.")
        else:
            print("The cost of your ticket is $15.")

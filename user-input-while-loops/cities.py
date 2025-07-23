prompt = "\nPlease enter the name of the city you've visited."
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt).lower()
    if city == 'quit':
        break
    else:
        print("I would love to go to " + city.title() + "!")

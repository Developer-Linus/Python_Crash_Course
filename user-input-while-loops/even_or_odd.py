number = input("Enter a number, I'll tell you if it is odd or even ")
number = int(number)

if number % 2 == 0:
    print('\nThe number' + str(number) + " is even.")
else:
    print('\nThe number ' + str(number) + " is odd.")

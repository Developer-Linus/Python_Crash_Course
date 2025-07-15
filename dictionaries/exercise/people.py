people = [
    {"alias": "linos", "name": "Linus Kipkemoi Langat", "age": 28},
    {"alias": "benso", "name": "Benson Mukuha Ngatia", "age": 24},
    {"alias": "sultan", "name": "Grant Ombongi Nyamweya", "age": 25},
]

for person in people:
    print("\n" + person['alias'].title() + "'s information is: ")
    print("\tName: " + person['name'].title())
    print("\tAge: " + str(person['age']))

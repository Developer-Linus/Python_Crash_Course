bella = {
    "kind": "dog",
    "owner": "Alice"
}

max = {
    "kind": "cat",
    "owner": "Brian"
}

luna = {
    "kind": "parrot",
    "owner": "Cynthia"
}

rocky = {
    "kind": "rabbit",
    "owner": "David"
}

milo = {
    "kind": "hamster",
    "owner": "Ella"
}

daisy = {
    "kind": "turtle",
    "owner": "Frank"
}

charlie = {
    "kind": "fish",
    "owner": "Grace"
}
pets = [bella, max, luna, rocky, milo, daisy, charlie]

for pet in pets:
    print("\tI am a " + pet['kind'] + ". My owner is " + pet['owner'])

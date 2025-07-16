favorite_places = {
    "Linus": [
        "Nairobi",
        "Machakos",
        "Kiambu",
    ],
    "Grant": [
        "Kisii",
        "Nairobi",
        "Nyamira",
    ],
    "Benson": [
        "Nanyuki",
        "Nairobi",
        "Machakos",
    ],
}

for name, places in favorite_places.items():
    print("\nI am " + name)
    print("My favorite places in Kenya are:")
    for place in places:
        print("\t" + place)

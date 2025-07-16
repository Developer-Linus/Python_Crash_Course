cities = {
    "nairobi": {
        "country": "Kenya",
        "population": 4397000,
        "fact": "It is known as the 'Green City in the Sun'.",
    },
    "tokyo": {
        "country": "Japan",
        "population": 13960000,
        "fact": "It is the most populous metropolitan area in the world",
    },
    "paris": {
        "country": "France",
        "population": 2161000,
        "fact": "It is known as the 'City of Light'",
    },
}
for city, information in cities.items():
    print("\nThe information about " + city.title())
    for type, data in information.items():
        print("\t" + type + " : " + str(data) + ".")

def build_person(first_name, last_name, age="", occupation=""):
    person = {"first": first_name, "last": last_name}
    if age:
        person['age'] = age
    if occupation:
        person['occupation'] = occupation
    return person


person = build_person("Linus", "Langat", 28, "software engineer")
print(person)

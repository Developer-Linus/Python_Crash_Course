def build_person(first_name, last_name):
    """Return a dictionary of a person"""
    person = {"first": first_name, "last": last_name}
    return person


person = build_person("Linus", "Langat")
print(person)

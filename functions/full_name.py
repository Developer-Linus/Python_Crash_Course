def get_formatted_name(first_name, last_name, middle_name=""):
    """Return full name, neatly formatted"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


name = get_formatted_name("Linus", "Langat", "Kipkemoi")
print(name)

def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")

"""
The definition of this functions specifies that we have to give
animal type and its name. When we are calling we need to specify based
on this order."""

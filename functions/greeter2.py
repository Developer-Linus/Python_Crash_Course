# Using while loop with a function

def get_formatted_name(f_name, l_name):
    full_name = f_name + " " + l_name + "."
    return full_name.title()


active = True
while active:
    print("\nPlease tell me your name")
    print("(Enter 'q' at any time to quit the program.)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name)

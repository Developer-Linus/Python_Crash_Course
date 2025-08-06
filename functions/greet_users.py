def greet_users(names):
    """
    Print a simple greeting to each user in a list
    """
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)


user_names = ["Hannah", "naomy", "calistus"]
greet_users(user_names)

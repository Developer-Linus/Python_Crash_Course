def print_magician_name(magicians):
    """
    Prints the name of each magician in magicians list
    """
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """
    Modifies the magician list by adding the phrase the great to each name
    """
    for i in range(len(magicians)):
        magicians[i] = f"{magicians[i]} the Great"


magicians = ['hellen', 'rusi', 'david']

make_great(magicians)
print_magician_name(magicians)

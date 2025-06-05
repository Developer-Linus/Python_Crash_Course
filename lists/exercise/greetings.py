names = ["Benson", "Grant", "Norbert", "Purity", "Amy", "Jeremy", "Rhoda"]

# More Pythonic and cleaner piece of code
for name in names:
    message = "Hello, " + name + ". Thank you for coming to the event."
    print(message)

# alternatively if I want to use indices
for i in range(len(names)):
    message = "Hello, " + names[i] + ". Thank you for coming to the event."
    print(message)

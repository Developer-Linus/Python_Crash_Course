# Stripping whitespace
'''
In some cases, we need to compare two strings, 'python ' and 'python' can be similar to us, but to programs they are totally different.
To address this challenge, python give us a method rstrip() or lstrip() to remove whitespaces on either right or left side of a string.
use strip() method to remove whitespaces from both sides of a string.
'''
favorite_language = "python "
print(favorite_language)
# Removes whitespace on the right side.
favorite_language.rstrip()
print(favorite_language)


# strip() method is used for cleaning user inputs before storing their values in the program.

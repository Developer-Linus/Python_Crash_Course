places = ["maldives", "usa", "germany", "egypt", "rwanda"]
print('\nOriginal list:')
print(places)
print("\nTemporarily sorted list:")
print(sorted(places))

print('\nOriginal list after temporary sorting:')
print(places)

places.reverse()
print('\nReversed list:')
print(places)

places.reverse()
print('\nList after applying double reversing:')
print(places)

places.sort()
print('\nPlaces in alphabetical order:')
print(places)

places.sort(reverse=True)
print('\nPlaces in reverse alphabetical order:')
print(places)

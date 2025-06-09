guests = ['Clement', 'Purity', 'Ezra', 'Gilbert', 'Memo', 'Amy']

print("Sorry, I can only invite two individuals to the party due to space constraints.\n")

removed_person1 = guests.pop(0)
print("Sorry, " + removed_person1 + " you can't attend the party.")
removed_person2 = guests.pop(2)
print("Sorry, " + removed_person2 + " you can't attend the party.")
removed_person3 = guests.pop(3)
print("Sorry, " + removed_person3 + " you can't attend the party.")
removed_person4 = guests.pop(0)
print("Sorry, " + removed_person4 + " you can't attend the party.\n")

print(guests[0] + ", you're still part of the the invited guests.")
print(guests[1] + ", you're still part of the the invited guests.")


del guests[1]
del guests[0]

print("---------------")

print(guests)

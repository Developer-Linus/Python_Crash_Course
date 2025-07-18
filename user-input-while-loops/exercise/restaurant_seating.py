number_of_people = input(
    "Tell me the number of people in your dinner group so that I check the table availability: "
)
number_of_people = int(number_of_people)
if number_of_people > 8:
    print("\nPlease wait for a table.")
else:
    print("\nYour table is ready.")

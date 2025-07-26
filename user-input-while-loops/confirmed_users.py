# Start with a list of unconfirmed users
# Create an empty list for holding confirmed users.

unconfirmed_users = [
    "nehemiah",
    "linus",
    "betty",
    "purity",
]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Displaying verified users
print("\nThe following are verified users:")
for user in confirmed_users:
    print(user.title())

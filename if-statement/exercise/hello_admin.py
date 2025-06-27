usernames = ['admin', 'user1', 'user2']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("\nHello " + username.lower() +
                  " would you like to see a status report?")
        else:
            print("\nHello " + username.lower() + " thank you for logging in.")
else:
    print('We need to find some users!')

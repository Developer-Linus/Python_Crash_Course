current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['USER1', 'user6', 'user7', 'user8', 'user9']

for user in new_users:
    if user.lower() in current_users:
        print(user + ' has already been taken!')
    else:
        print(user + ' is available for use.')

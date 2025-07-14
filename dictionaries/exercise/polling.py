favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
names = ["jen", 'phil', 'bowen', 'gilbert']
for name in names:
    if name in favorite_languages.keys():
        print(name.title() + " , thank you for participating in this poll.")
    else:
        print(name.title() + ", please take our poll.")

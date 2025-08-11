class User:
    def __init__(self, first_name, last_name, age, email, location):
        """
        Constructor method for creating instance of a user with
        first_name, last_name, age, location, and email
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        """
        Give information about user
        """
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Location: {self.location}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """
        Greets user with personalized message
        """
        print(
            f"Hello {self.first_name.title()} {self.last_name.title()}. We will be in {self.location.title()}. Get ready you meet your amazing team.")


user1 = User("Alice", "Johnson", 28, "alice@example.com", "New York")
user2 = User("Brian", "Smith", 35, "brian@example.com", "London")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

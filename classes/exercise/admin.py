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


class Privileges:
    def __init__(self, privileges: list[str] | None = None) -> None:
        self.privileges = privileges if privileges is not None else []

    def show_privileges(self) -> None:
        print(f"Admin privileges: {self.privileges}")

    def add_privilege(self, privilege: str):
        self.privileges.append(privilege)


class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, email: str, location: str):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()


# Create an Admin instance
admin_user = Admin(
    first_name="Alice",
    last_name="Johnson",
    age=35,
    email="alice.admin@example.com",
    location="London"
)
# Add privileges dynamically
admin_user.privileges.add_privilege("can add user")
admin_user.privileges.add_privilege("can delete user")
admin_user.privileges.add_privilege("can ban user")
admin_user.privileges.show_privileges()

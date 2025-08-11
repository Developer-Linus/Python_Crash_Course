class Car:
    """
    Model for a car
    """

    def __init__(self, make, model, year):
        """Initialize car attributes"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model + "."
        return long_name


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

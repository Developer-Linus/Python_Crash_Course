class Car:
    """
    Model for a car
    """

    def __init__(self, make, model, year):
        """Initialize car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model + "."
        return long_name

    def read_odometer_reading(self):
        """Prints a statement showing car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the give value
        Rejects change if you want to rollback odometer
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot rollback an odometer.")

    def increment_odometer(self, miles):
        """Incremente odometer based on given miles"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You cannot roll back odometer.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Modify the attribute value directly in its instance
my_new_car.odometer_reading = 23
# Modify the attribute value using a method
my_new_car.update_odometer(23)
my_new_car.increment_odometer(23500)
my_new_car.read_odometer_reading()

class Restaurant:
    """
    Class for creating restaurant based on restaurant name and cuisine type
    Has got two methods: one for describing restaurant and one for informing that the restaurant is open
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initializes restaurant instance with restaurant name and cuisine type
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """
        Provide information about the name and cuisine type offered by restaurant
        """
        print("The name of the restaurant is " + self.restaurant_name.title())
        print("The cuisine type it offers is " + self.cuisine_type)

    def open_restaurant(self):
        """
        Informs that the restaurant is open.
        """
        print("The restaurant is open. You're welcome to enjoy your cuisine.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str, flavors: list[str] | None = None):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)

    def display_flavors(self):
        if self.flavors:
            print(f"Ice cream flavours available: {self.flavors}")
        else:
            print("There are no flavors in the stand at the moment")


icecream_stand = IceCreamStand("Sweet Treats", "Ice Cream", [
                               "Vanilla", "Chocolate"])
icecream_stand.display_flavors()

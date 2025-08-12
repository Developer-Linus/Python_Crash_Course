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
        self.number_served = 0

    def set_number_served(self, customers):
        """
        Sets the number of customers served by restaurant
        """
        if customers > self.number_served:
            self.number_served = customers
        else:
            print("You cannot add no customer.")

    def increment_number_served(self, customers):
        """
        Increments the number of customers by specific number
        """
        if customers > 0:
            self.number_served += customers
        else:
            print("You can add customers if only you've new ones.")

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


restaurant = Restaurant('The Spice Garden', 'Indian')
restaurant1 = Restaurant('La Tavola Rustica', 'Italian')
restaurant2 = Restaurant('Savor Seoul', 'Korean')
restaurant3 = Restaurant('Nyama Fusion Grill', 'African')

print(restaurant1.number_served)

restaurant1.set_number_served(25)
print(restaurant1.number_served)
restaurant1.increment_number_served(34)
print(restaurant1.number_served)

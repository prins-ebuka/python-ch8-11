from dog import Restaurant

#My attempt at the Exercise 9-6
class IceCreamStand(Restaurant):
    """A simple class that derives from the class Restaurant."""
    def __init__(self, name, cuisine, *flavors):
        """Initializing the attributes of the parent class."""
        super().__init__(name, cuisine)
        self.flavors = flavors

    def display_flavors(self):
        """A simple attampt to display the flavors in the restaurant."""
        print(f"The flavors available are {self.flavors}.")

#Creating an instance of the IceCreamStand
my_icecreamstand = IceCreamStand("Icy", "Ice Cream", "Vanilla", "Blueberry", "Orange")

my_icecreamstand.display_flavors()
my_icecreamstand.describe_restaurant()

#The output still brings out what is in dog.py. I need to figure out how to stop this.
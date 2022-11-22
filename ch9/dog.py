class Dog:
    """A simple  attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#Try it yourself
class Restaurant:
    """A simple attempt to model a Restaurant."""

    def __init__(self, name, cuisine):
        """Initializing the attributes of the Restaurant."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Pieces of information of our restaurant."""
        print(f"{self.name} is the name of the restaurant with cuisine type {self.cuisine}.")

    def open_restaurant(self):
        """Tell customers that the restaurant is open."""
        print(f"{self.name} is open for your service.")

my_restaurant = Restaurant('Grant Thornton', 'Pizza')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


class User:
    """A simple attempt to describe a user."""

    def __init__(self, first_name, last_name, *other_info):
        """Initialize the attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.other_info = other_info

    def describe_user(self):
        """Summary of the user information."""
        if self.other_info:
            print(f"This users name are first name: {self.first_name.title()}, last name: {self.last_name.title()}, other info: {self.other_info}.")
        else:
            print(f"This users name are first name: {self.first_name.title()}, last name: {self.last_name.title()}.")

    def greet_user(self):
        """A simple greeting."""
        print(f"Hello {self.last_name.upper()}, {self.first_name.title()}!")

my_user = User('emmanuel', 'ihekwereme', 'igbo', 'average height')
my_user.describe_user()
my_user.greet_user()

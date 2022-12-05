def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
#This is called calling a function multiple times
#Also, order matters in positional arguments.

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

#when using keyword arguments, be sure to use the exact names of the parameter.

#Default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('willie')
#because we are using a default value, the order is changed in the function definition, this...
#is interpreted by Python as a positional argument and thus one argument is left which is the pet_name
describe_pet(pet_name='harry', animal_type='hamster')
#when you use default values, values with default values have to be listed last.

#Try it yourself
def make_shirt(size, text='I love Python'):
    """Display information about the shirt."""
    print(
        f"The size of the shirt is {size}. Here is the message printed on the text, {text}."
        )

make_shirt(6, 'mad_man')
make_shirt(text='alaye', size='9')
make_shirt('large')


from random import randint 
#Try it yourself

class Die:
    """A simple attempt to make a die/dice."""

    def __init__(self, sides=6):
        """Initializing the attributes of the die/dice."""
        self.sides = sides

    def roll_die(self):
        """A method to print a random number."""
        return randint(1, self.sides)

#Make a 6-sided die, and roll it 10 times and show the results
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

#Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("10 rolls of a 10-sided die:")
print(results)

#Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("10 rolls of a 20-sided die:")
print(results)
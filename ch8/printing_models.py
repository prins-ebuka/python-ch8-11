#Start with some designs that needs to be printed

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedro']
completed_models = []

#Simulate printing each design until none is left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#We can make this better structured by putting it in a function
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none is left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodechadron']
completed_model = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#to work with the copy, use the slice notation
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
#Preferably work with the original list instead of a copy as this saves time.

#Try it yourself

 
def show_msgs(short_msgs, main_holder):
    """Return a neatly formatted greeting from a list."""
    while short_msgs:
        holding_msg = short_msgs.pop()
        print(f"{holding_msg}")
        main_holder.append(holding_msg)

def send_msgs(main_holder):
    """Return the new list from short msgs."""
    for holder in main_holder:
        print(holder)

a = ['hi', 'hello', 'greetings', 'goodday']
b = [] 

show_msgs(a, b)
send_msgs(b)

show_msgs(a[:], b)
send_msgs(b)
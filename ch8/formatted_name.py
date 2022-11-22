#Return Values 
#(i)A function doesn't always have to display its output directly. Instead it can process a set...
#of values and then return a value or set of values
#(ii)The return statement takes a value from inside a function and sends it back to the line that called the function

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

get_formatted_name('jimi', 'hendrix')
#I noticed that this cannot print because of the absence of the print function.
print(get_formatted_name('jimi', 'hendrix'))

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hooker', 'lee')
print(musician)
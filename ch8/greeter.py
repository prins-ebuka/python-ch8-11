def greet_user():
    """Display a single greeting."""
    print("Hello!")

greet_user()

def greet_user(username):
    """Display a single greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

#Try it yourself
def display_message():
    """Print a sentence about what I am learning."""
    print('I am learning about functions.')

display_message()

def favourite_book(title):
    """Print a message about my favourite book."""
    print(f"One of my favourite books is {title.title()}.")

favourite_book('deep work')

#Using a Function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#This is an infinite loop
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    #Try it yourself#
def city_country(city, country):
    """Return a neatly formatted city and country."""
    print(f"{city.title()}, {country.title()}")

city_country('lagos', 'nigeria')

def make_album(artist_name, album_name, number=None):
    """Return a dictionary of an album and its artist."""
    if number:
        song_details = {'artiste': artist_name, 'album': album_name, 'number': number}
    else:
        song_details = {'artiste': artist_name, 'album': album_name}
    return song_details

#Prepare the prompts
title_prompt = 'what album are you thinking of?'
artist_prompt = "Who's the artist?"

#Quit condition
print("Enter 'q' at anytime to quit")
while True:
    title = input(title_prompt)
    if title == 'q':
        break

    artist = input(artist_prompt)
    if artist == 'q':
        break

    album = make_album(artist, title)
    print(album)


song_detail = make_album(1985, 'J Cole',5)
song_details = make_album('Drake', 'Switch')
print(song_detail)
print(song_details)

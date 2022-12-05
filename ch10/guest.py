#Try it yourself 10-3
name = input('Kindly provide your name:')

username = (name)

with open('guest.txt', 'w') as user:
    user.write(f"{username}")

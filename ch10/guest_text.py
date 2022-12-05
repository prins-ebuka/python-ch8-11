#Try it yourself: Exercise 10-4
while True:
    name = input("Kindly provide your name:")
    if name != 'q':
        print("Thanks, for providing your name!")
    else:
        break

    with open('guest_book.txt', 'a') as username:
        username.write(f"{name}, visited this file.\n")

#Try it yourself: Exercise 10-5
while True:
    survey = print("Why do you like programming?")
    response = input('')
    if response != 'q':
        with open('programming_poll.txt', 'a') as responses:
            responses.write(f"{response}.\n")
    else:
        break
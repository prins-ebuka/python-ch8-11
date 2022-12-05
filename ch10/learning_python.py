#Try it yourself - Exercise 10-1

with open('learning_python.txt') as file_objects:
    contents = file_objects.read()

print('\tReads and prints the file three times')
print(contents)

print('\tLooping over the lines')
with open('learning_python.txt') as file_objects:
    for line in file_objects:
        print(line.strip())

print('\tStoring the lines in a list')
with open('learning_python.txt') as file_objects:
    lines = file_objects.readlines()

for line in lines:
    print(line.strip())


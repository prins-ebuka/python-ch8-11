with open('learning_python.txt') as f:
    contents = f.read()
    
new_file = contents.replace('Python', 'C')
print(new_file)
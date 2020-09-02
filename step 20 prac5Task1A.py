finished = False

while finished != True:
        value = int(input("Enter a value to be cubed."))
        cube = value ** 3
        print(value, "cubed is", cube)
        choice = int(input("Cube another number?"))
        if choice == 'no':
            finished = True

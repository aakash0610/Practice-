def main():
    name = str(input("Please enter your name: "))
    while name == '':
        print("please enter a valid name")
        name = str(input("Please enter your name: "))

    current_sal = int(input("Please enter your current salary: "))
    while current_sal == '':
        print("please enter a valid NUMBER")
        current_sal = int(input("Please enter your current salary: "))

    new_sal = current_sal + (current_sal * (4.5/100))
    print('your salary after 4.5 raise will be: '+str(new_sal))
main()

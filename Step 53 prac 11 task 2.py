def main():
    name = str(input("please enter your name: "))
    while name == '':
        print("please enter a valid input")
        name = str(input("please enter your name: "))

    age = int(input("please eneter your age: "))
    while not (age in range(1,100)):
        print("please enter a valid input")
        age = int(input("please eneter your age: "))

    new_age = age + 8
    print("your age after 8 years is " + str(new_age))


main()

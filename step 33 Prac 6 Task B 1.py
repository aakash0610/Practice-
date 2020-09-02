def menu():
    enter = main("(S)miley\n(F)rowny\n(Q)uit".upper())
    while enter != 'q'.upper():
        display(enter)
        enter = main("(S)miley\n(F)rowny\n(Q)uit".upper())
    print("Thank You and Adios!")

def main(prompt):
    enter = str(input(prompt).upper())
    return enter


def display(enter):
    if enter == "S":
        print(":)")
    elif enter == "F":
        print(":(")
    elif enter == "Q":
        print("Thank You and Adios!")
    else:
        print("Invalid Choice!")


menu()

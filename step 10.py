def main():
    colour = str(input("please enter a primary colour:"))
    colour_2 = str(input("please enter a primary colour:"))
    if colour == 'red' and colour_2 == 'yellow':
        print("orange")
    elif colour == 'yellow' and colour_2 == 'red':
        print("orange")
    elif colour == 'blue' and colour_2 == 'red':
        print("purple")
    elif colour_2 == 'blue' and colour == 'red':
        print("purple")
    elif colour == 'blue' and colour_2 == 'yellow':
        print("green")
    elif colour_2 == 'blue' and colour == 'yellow':
        print("green")
    else:
        print("*ERROR* Please enter either red, blue or yellow")


main()

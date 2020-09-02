def main():
    CS101 = {"Room Number: 3004", "Lecturer name: Haynes", "Time : 8 AM"}
    CS102 = {"Room Number: 4501", " Lecturer name: Alvarado", "Time : 9 AM"}
    CS103 = {"Room Number: 6755", "Lecturer name: Rich", "Time : 10 AM"}
    NT110 = {"Room Number: 1244", "Lecturer name: Burke", "Time : 11 AM"}
    CM241 = {"Room Number: 1411", "Lecturer name: Lee", "Time : 1 PM"}

    print("the choices are: ")
    number = int(input("1. CS101 \n2. CS102 \n3. CS103 \n4. NT110 \n5. CM241 \n6. Quit"))
    if number == 1:
        print(CS101)
    elif number == 2:
        print(CS102)
    elif number == 3:
        print(CS103)
    elif number == 4:
        print(NT110)
    elif number == 5:
        print(CM241)
    elif number == 6:
        print("Thank You")


main()

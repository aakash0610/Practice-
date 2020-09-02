def leap_year():
    year = int(input("Enter year "))
    cal(year)


def cal(year):
    if year % 4 == 0 and year % 100 != 0:
        print("its a leap year")
    elif year % 400 == 0:
        print("its a leap year")

    else:
        print("not one")

leap_year()
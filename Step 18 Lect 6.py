def main():
    print("Welcome to Tropical Auto")
    name = str(input("Please enter your name: "))
    age = int(input("please enter your age: "))
    car = str(input("please choose your car type: [C]: Hatchback (25$), [S]: SUV (40$) , [H]: Hummer (100$) ")).lower()
    while car not in ["c","s","h"]:
        print("car type must be c, s or h")
        car = str(input("please choose your car type: [C]: Hatchback (25$), [S]: SUV (40$) , [H]: Hummer (100$) ")).lower()

    days = int(input("Please enter number of days for rental: "))
    while days == 0:
        print("Sorry days for rental must be greater than 0.")
        days = int(input("Please enter number of days for rental: "))
    print("Thank You for reservation.")

    c = 25
    s = 40
    h = 100
    if car == c:
        base_price = c * days
    elif car == s:
        base_price = s * days
    else:
        base_price = h * days

    if age< 25:
        youth_tax = 0.3 * days
    else:
        youth_tax = 0
    total = youth_tax+ base_price
    print("Your total is as follow:\n " ,"base rental is: "+str(base_price) + "\n youth tax is: " +str(youth_tax)+ "\n total rental cost is: " +str(total))


main()

def main():
    weight = int(input("please enter the weight of your parcel: "))
    if weight <= 2:
        price = str(weight * 1.10)
        print("the charge is $1.10 per Kg, thus your total amount is: " + price)
    elif 2 < weight < 6:
        price = str(weight * 2.20)
        print("the charge is 2.20 per Kg, thus your total amount is: " + price)
    elif 6 <= weight < 10:
        price = str(weight * 3.70)
        print("the charge is 3.70 per Kg, thus your total amount is: " + price)
    else:
        price = str(weight * 3.80)
        print("the charge is 3.80 per Kg, thus your total amount is: " + price)


main()

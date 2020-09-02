def main():
    coffee = int(input("please enter the number of coffee cups you would like to order: "))
    while coffee < 0:
        print("error")
        coffee = int(input("please enter the number of coffee cups you would like to order: "))

    tshirt = int(input("please enter the number of tshirts you would like to purchase: "))
    hdd= int(input("please enter the number of HDD you would like to purchase: "))

    total_coffee = coffee*5
    total_thsirt = tshirt*15
    total_hdd = hdd*100
    total = total_coffee+ total_hdd+ total_thsirt

    if total < 150:
        charges = 3*coffee + 3*tshirt + 3*hdd
        sum = total + charges
        print(sum)
    else:
        print(total)
main()
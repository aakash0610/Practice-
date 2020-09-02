def main():
    total = 0
    num_items = int(input("Please enter the number of items bought: "))

    while num_items <= 0:
        print("Please enter a valid input!")
        num_items = int(input("Please enter the number of items bought: "))

    for i in range (0,num_items):
        priceItem = float(input("Please enter the price of the item: "))
        total += priceItem
    print("total price for " +str(num_items)+ " is : {:.2f} $".format(total))

    if total > 100:
        dis = total* 0.1
        new_total = total - dis
        print("total price for " +str(num_items)+ " is : {:.2f} $".format(total) +" with discount of 10% your new "
                                                                                  "total is:  {:.2f}".format(new_total) + "$")

main()
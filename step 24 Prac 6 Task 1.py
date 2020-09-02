def main():
    housecost = int(input("Enter House cost: "))
    landSize = int(input("Enter Land Size: "))
    landCost = int(input("Enter cost of land per sq meters: "))
    totalLandCost = landSize * landCost
    totalCost = totalLandCost +housecost
    print("total cost for land is: " + str(totalLandCost))
    print("total cost is : " + str(totalCost))

main()
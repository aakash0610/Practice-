# Write a function for checking the speed of drivers. This function should have one parameter: speed. If speed is
# less than 70, it should print “Ok”. Otherwise, for every 5km above the speed limit (70), it should give the driver
# one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print:
# “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”

speed = int(input("please enter the speed of your car: "))
if speed < 70:
    print("you are good to go")
elif 70 < speed < 75:
    print("demerit points: 1")
elif 75 < speed < 80:
    print("demerit points: 2")
elif 80 < speed < 85:
    print("demerit points: 3")
elif 85 < speed < 90:
    print("demerit points: 4")
elif 90 < speed < 95:
    print("demerit points: 5")
elif 95 < speed < 100:
    print("demerit points: 6")
elif 100 < speed < 105:
    print("demerit points: 7")
elif 105 < speed < 110:
    print("demerit points: 8")
elif 110 < speed < 115:
    print("demerit points: 9")
elif 115 < speed < 120:
    print("demerit points: 10")
elif 125 < speed < 130:
    print("demerit points: 11")
else:
    print("License suspended")

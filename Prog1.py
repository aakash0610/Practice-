def main():
    asleep = 40                                                                                                         # define hours of sleep required by a regular human
    total = 0

    for day_sleep in range(1, 6):                                                                                       #for days from 1 to 5
        day = int(input("Please enter day " + str(day_sleep) + " sleep: "))                                             #take input from user
        while day > 24:                                                                                                 #input cannot be greater than 24 for a day as there are only 24 hours in a day.
            print("Invalid Input")
            day = int(input("Please enter day " + str(day_sleep) + " sleep: "))
        total = total + day                                                                                             #take the total of days from 1 to 5
        sleep = asleep - total                                                                                          #tally it with regular persons sleep

    if asleep >= total:                                                                                                 #if the person slept for less than 40 hours print this
        print(
            "\nYour total hours of sleep were: " + str(total) + " \nYour sleep debt over this time is: " + str(
                sleep) + "\nYou need more sleep!")
    else:                                                                                                               #else
        print('Your total hours of sleep were ' + str(total) + "\n You sleep too much! I'm Jealous XD")


main()

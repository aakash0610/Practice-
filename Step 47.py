import random

name = str(input("What is your name? "))
print("Welcome " + name + "!")
print("Lets play golf, CP1401 style!")

par = int(input("choose a par for this course (number between 3-5 inclusive): "))
while not 5 >= int(par) >= 3:
    print("im sorry you must choose a number between 3-5 inclusive. please enter again")
    par = input("choose a par for this course (number between 3-5 inclusive): ")

hole = int(input("How many meters to the hole (between 195 - 250 inclusive) "))
while not hole in range(195, 250):
    print("invalid input! please")
    hole = int(input("please enter the distance to the hole (195 - 250 is the range): "))

score_list = []
round = []


def greetings():
    display = main_menu("Hola! \n(I)nstructions \n(P)lay Game \n(Q)uit")

    while display.lower() == 'i' or display.lower() == 'p':
        display = main_menu("Hola! \n(I)nstructions \n(P)lay Game \n(Q)uit")

    while not (display.lower() == 'i' or display.lower() == 'p' or display.lower() == 'q'):
        print("invalid option")
        main_menu("Hola! \n(I)nstructions \n(P)lay Game \n(Q)uit")


def game_play():
    print("the distance to the hole entered is: " + str(hole))
    shots_hit = 0
    new_distance = hole

    while new_distance != 0:
        swing_choice = str(input("\nwhich club would you like to choose: \n1. (D)river \n2. (I)ron \n3. (P)utter"))

        if swing_choice.lower() == 'd':
            score = int(random.randint(80, 120))
            print("Your shot went : " + str(score))
            new_distance = abs(new_distance - score)
            shots_hit += 1
            print("distance to the hole now is: " + str(new_distance))
            score_list.append(score)



        elif swing_choice.lower() == 'i':
            score = random.randint(24, 36)
            print("Your shot went : " + str(score))
            score_list.append(score)
            new_distance = abs(new_distance - score)
            shots_hit += 1
            print("distance to the hole now is " + str(new_distance))




        elif swing_choice.lower() == 'p':
            if new_distance < 10:
                dist = int(new_distance * 0.8)
                dist1 = int(new_distance * 1.2)
                score = random.randint(dist, dist1)
                print("Your shot went : " + str(score))
                score_list.append(score)
                new_distance = abs(new_distance - score)
                shots_hit += 1
                print("distance to the hole is " + str(new_distance))

            else:
                score = random.randint(8, 12)
                print("Your shot went : " + str(score))
                score_list.append(score)
                new_distance = abs(new_distance - score)
                shots_hit += 1
                print("distance to the hole is " + str(new_distance))



        else:
            print("Invalid club selection = Air Swing :( \n Your shot went 0m. Your are " + str(
                new_distance) + " m away after " + str(shots_hit))
            shots_hit += 1
            score_list.append(0)

    if new_distance == 0:
        print('clunk ... after ' + str(shots_hit) + ' hits your ball is in the hole! \nConragts! you are ' + str(
            shots_hit) + ' out of ' + str(par) + ' for this hole\nyour overall score is ' + str(
            shots_hit) + ' and you are ' + str(par) + " under par for this hole")
        round.append(shots_hit)

    return


def main_menu(prompt):
    display = input(prompt).lower()

    if display.lower() == 'i':
        instructions()

    elif display.lower() == 'p':
        print(game_play())

    elif display.lower() == 'q':

        for i in range(len(round)):
            if round[i] > int(par):
                print("Round " + str(i) + " shots: " + str(round[i]) + " over par by  " + str(abs(round[i] - par)))
            elif round[i] < int(par):
                print("Round " + str(i) + " shots: " + str(round[i]) + " under par by  " + str(abs(par - round[i])))
        print("Thank you")

    else:
        print("please choose between given options")

    return display


def instructions():
    print(
        "This is a simple golf game in which each hole is 230 meters game away with par 5. \nYou are able to choose "
        "from 3 clubs, the driver, iron or putter. \nThe driver will hit around 100 meters, the iron around 30 "
        "meters and the putter around 10 meters. \nThe putter is best used very close to the hole." "\n Driver : "
        "100m\nIron: 30m\nPutter: 10m")
    return


greetings()

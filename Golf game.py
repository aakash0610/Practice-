import random

def greetings():
    score = []
    name = input("what is your name?")
    print("welcome "+name)
    print("Lets play golf,CP1401 style!")

    par = input("Choose a par for this course (between 3-5 inclusive)")
    while 3<= par <=5:
        print("im sorry you must choose a number between 3-5 inclusive. Please enter again")
        par = input("Choose a par for this course (between 3-5 inclusive)")

    hole = input("how many meters to the hole? (between 195 - 250 inclusive)")

    enter = input("\n(I)nstructions \n(P)lay round \n(Q)uit")
    while enter != 'i' or 'p' or 'q':
        print("invalid menu choice")
        enter = input("\n(I)nstructions \n(P)lay round \n(Q)uit")

    if enter == 'i':
        instructions()

    elif enter == 'p':



        def play_game():
            shots_hit = 0
            print("THis hole is "+hole+"par"+par)
            choice = input("Club Selection: \nPress D for Driver \nI for Iron \nP for Putter")
            print("Club selection: "+choice)
            distance_to_hole = hole
            while distance_to_hole != 0:
                #error handling

                if choice.lower() != 'd' or 'i' or 'p':
                    print("invalid club selection - air swing :(")
                    print("your shot went 0m")
                    score.append(0)
                    shots_hit+=1

                if choice.lower() == 'd':
                    shots_hit+=1
                    current_score = random.randint(80,121)
                    print("Your shot went "+current_score+" m after "+shots_hit)
                    distance_to_hole = abs(hole - current_score)
                    score.append(current_score)

                elif choice.lower() == 'i':
                    shots_hit+=1
                    t_score = random.randint(24,37)
                    distance_to_hole = abs(distance_to_hole - t_score)
                    print("your shot went"+t_score+" m after"+shots_hit)
                    score.append(t_score)

                elif choice.lower() == 'p':
                    shots_hit +=1
                    p_score = random.randint(8,12)
                    distance_to_hole = abs(distance_to_hole - p_score)
                    print("your shot went"+p_score+" m after"+shots_hit)
                    score.append(p_score)






def instructions():
    print(
                "This is a simple golf game in which each hole is 230 meters game away with par 5. \nYou are able to choose "
                "from 3 clubs, the driver, iron or putter. \nThe driver will hit around 100 meters, the iron around 30 "
                "meters and the putter around 10 meters. \nThe putter is best used very close to the hole." "\n Driver : "
                "100m\nIron: 30m\nPutter: 10m")
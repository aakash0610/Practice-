from random import randint
def main():
    print("Game is to guess the number ")
    num = int(input("Please enter a number between 0 to 10 : "))
    min = 0
    max = 10
    for i in range(1):
        random = randint(min, max)
        if random == num:
            print("Number you guessed is the same! Congrats :)")
        else:
            print("Ohh the number you guessed is wrong! :( the correct one is : " +str(random))
            break
    re =input("Would you like to try again? if so please hit enter")
    if re == '':
        main()
    else:
        exit()

main()
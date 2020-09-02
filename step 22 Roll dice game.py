#roll dice game

from random import randint
print("Hit Enter to Start!")
i = input('')
def main():
    min =1
    max = 6
    while min:
        random = randint(min, max)
        print(random)
        break
    re = input("If you want to roll again hit enter")
    if re == '':
        main()
    else:
        exit()


main()

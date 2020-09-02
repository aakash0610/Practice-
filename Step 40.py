import random

def main():
    count= 0
    for i in range(1, 101):
        number = random.randint(1, 1000)
        if is_even(number):
            count = count +1
    print (count)


def is_even(number):
    if number % 2 == 0:

        return True
    else:
        return False


main()

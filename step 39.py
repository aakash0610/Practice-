G = 9.8


def main():
    for i in range(1, 11):
        print(fallingDistance(i))


def fallingDistance(time):
    distance = (1 / 2) * (G * (time) ** 2)
    return distance


main()

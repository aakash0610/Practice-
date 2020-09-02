from random import randint


def main():
    print("Welcome to tropical bowling!")
    running_total = 0
    for frame_num in range(1, 11):
        print("Frame ", frame_num)

        ball_one = randint(0, 10)
        print("ball 1: ", ball_one)

        remaining_pins = 10 - ball_one
        ball_two = randint(0, remaining_pins)
        print("ball 2: ", ball_two)

        frame_total = ball_one + ball_two
        print("Frame total: ", frame_total)

        running_total += frame_total
        print("current total: ",format(running_total))


main()

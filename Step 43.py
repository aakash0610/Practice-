PER = []


def main():
    i = 0
    for i in range(0, 5):
        no = int(input("Enter yor grade between 0 and 100: "))
        if 0 < no <= 100:
            PER.append(no)
            i += 1
        else:
            print("invalid number")
            no = int(input("Enter yor grade between 0 and 100: "))
    print(PER)
    avg = calc_average(PER)
    print(avg)
    print(determine_grades(avg))


def calc_average(PER):
    avg = sum(PER)/ 5
    return avg


def determine_grades(avg):
    if avg < 50:
        print("F")
    elif 50 < avg < 64:
        print("P")
    elif 65 < avg < 74:
        print("C")
    elif 75 < avg < 84:
        print("D")
    elif 85 < avg <= 100:
        print("HD")


main()

def main():
    import random
    Australia_states_capitals = {
        "Australia and Australian Capital Territory": "Canberra",
        "New South Wales": "Sydney",
        "Victoria": "Melbourne",
        "Queensland": "Brisbane",
        "Western Australia": "Perth",
        "South Australia": "Adelaide",
        "Tasmania": "Hobart",
        "Northern Territory": "Darwin"
    }
    print("Answer the Capital of following state:\n")
    count = 0
    count1 = 0
    for x in range(0, 8):
        k = random.choice(list(Australia_states_capitals.items()))
        print(k[0])
        x = input("Enter the answer:\n")
        if (x == k[1]):
            count = count + 1
            print("Correct")
            continue
        else:
            count1 = count1 + 1
            print("Incorrect")
            continue

    print("The total number of correct answers are:", count, "\n")
    print("The total number of incorrect answers are:", count1, "\n")


main()
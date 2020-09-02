def main():
    age = int(input("Enter your age: "))
    enrolled = input("Are you enrolled to vote (Y/N)? ").upper()
    if age >= 18 and enrolled == 'Y':
        print("you may vote")
    elif age >= 18 and enrolled == 'N':
        print("you are not eligible to vote")
    else:
        print("GO HOME")


main()
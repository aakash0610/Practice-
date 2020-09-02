def main():
    number = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    specialchar = "  =", "+", "`", "~", ".", "/", "'", "[", "]", "<", ">", "?", "{", "}", "|", "$"
    name = input("Please enter a password : ")
    upper = False
    numb = False

    while len(name) < 6 or numb == False or upper == False or name in specialchar:
        print("Invalid Password. Password should contain at least one special character, one Upper case letter and "
              "length should be greater than 6 ")

        for i in name:
            if i.isupper():
                upper = True

        for i in number:
            if i.isdigit():
                numb = True

        if upper == False:
            print("there is no upper case letter in password")
        if numb == False:
            print("there is no number in password")

        name = str(input("Please enter a password : "))

    print("gaiudaishdb")


main()

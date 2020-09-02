def name():
    digit = 0
    letter =0
    write = input("please enter ")
    char = '$', '@', '!', '#', '%', '&', '*', '-', '+', '=',''

    for char in write:
        pass

    print("total length: "+str(len(write)))

    for i in write:
        if i.isdigit():
            digit += 1
    print("Digits: "+str(digit))

    for i in write:
        if i.isalpha():
            letter+=1
    print("letters: "+str(letter))
name()

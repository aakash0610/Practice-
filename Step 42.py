def get():
    list = []
    for i in range(6):
        no = int(input("Please Enter number " + str(i) + ":"))
        list.extend(str(no))
    i += i
    list.sort()
    print(*list, sep="\n")


get()

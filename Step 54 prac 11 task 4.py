def filename():
    details = []
    file_name = str(input("please input your file name: "))
    name = str(input("please enter your name: "))
    age = int(input("please enter your age"))
    add = str(input("please enter your address: "))

    NAME = file_name + '.txt'
    f = open(NAME, 'w+')
    while name == '':

        f.write('%s , %d , %s' % (name, age, add))
        f.close()


filename()

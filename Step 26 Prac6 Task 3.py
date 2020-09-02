names =[]
year = []
for i in range(2):
    name = input("What is your name: ")
    names.append(name)
    year_of_birth = int(input("Which year were you born: "))
    retirement = year_of_birth + 70
    year.append(retirement)
print("{} will become eligible in {}".format(name[0], year[0]) + "{} will be eligible in {}".format(name[1],year[1]))

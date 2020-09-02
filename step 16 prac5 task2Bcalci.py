# test avg calculator

def main():
    num_students = int(input("enter number of students: \n"))
    scores = int(input("how many test scores per student?: \n"))
    total = 0
    x = 0
    y = 0
    for y in range(num_students):
        y += 1
        total = 0
        name = str(input("Please enter student name: "))
        for x in range(1, scores + 1):
            test = int(input("Enter result for " + str(x) + " test:"))
            total += test
        x += 1
        avg = total / scores
        print(name, "\nthe average for " + str(y) + " is : " + str(avg))


main()

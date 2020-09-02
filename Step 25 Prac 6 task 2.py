height = float(input("Please enter Height in meters: "))
weight = int(input("Please enter Weight in kgs: "))


def cal():
    bmi = (weight / height ** 2)
    print("your BMI is : {:.2f}".format(bmi))


cal()
cal()

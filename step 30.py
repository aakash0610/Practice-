def num():
    lhs = add("enter a number: ")
    rhs = add("Enter a number: ")
    display(lhs, rhs)


def add(prompt):
    int_num = int(input(prompt))
    return int_num


def display(int_num1,int_num2):
    sum = int_num1 + int_num2
    product = str(int_num1*int_num2)
    div = str(int_num1**int_num2)
    print("sum of "+str(int_num1) +" and "+str(int_num2) +"is : " +str(sum))
    print("product of "+str(int_num1) +" and "+str(int_num2) +"is : " +str(product))
    print("power of "+str(int_num1) +" and "+str(int_num2) +"is : " +str(div))

num()
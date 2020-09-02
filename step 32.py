num = []
for i in range(3):
    num1 = int(input("enter a number"))
    num.append(num1)
num[0], num[1] =num[1] , num[0]
multiply = num[0]* num[2]
sum = num[1] + num[2]
print(multiply,sum)

def check_bal():
    pay = int(input("Please enter outstanding balance : "))
    while not 0 < pay <= 5000:
        print("outstanding balance should be between 0 to 5000$")
        pay = int(input("Please enter outstanding balance : "))
    min_repayment = str(pay*.1)
    repay = input('enter your repayment :')
    while repay < str(min_repayment):
        print("payment must be atleast 10% of outstanding balance")
        repay = input('enter your repayment :')
    new_bal = pay - int(repay)
    print("remaining balance is  "+str(new_bal))
check_bal()
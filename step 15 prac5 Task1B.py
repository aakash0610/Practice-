# avg rainfall

years = int(input("Please enter number of years: "))
total = 0
avg = 0
for i in range(years*12):
     months = int(input("Please enter the rainfall this month: "))
     total +=months
     avg = total/12
print("number of months: " + str(years*12))
print("total inches of rainfall is: " +str(total))
print("avg rainfall per month is:" + str(avg))
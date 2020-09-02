MAX_SETS = 5
MAX_NUMBERS = 2

sum = 0;
total = 0;

for set in range(1,MAX_NUMBERS + 1):
   for number in range(1, MAX_SETS + 1):
      value = int(input("Enter number " +str(number)+ " of set "+ str(set)+ ":"))
      sum = sum + number
   print("The sum of set", set, "is", sum, ".")
   total = total + sum
   sum = 0

print("The total of all the sets is ", total, ".")

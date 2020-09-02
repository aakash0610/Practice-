a = []
for x in range(7):
    day = str(input("enter day:"))
    bugs = int(input("enter number of bugs collected on " +day + ":" ))
    a.append(bugs)
print("Total number of BUGS collected this entire week are: " ,sum(a[0:len(a)]))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for x in list(a):  # check list a for a num
    if x in list(b):  # check if that same num is in list b
        c.append(x)  # if both are true then add that num in list c
        print(c)
print(sum(c[0:len(c)]))  # sum of the numbers in the list

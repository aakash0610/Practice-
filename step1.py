no = int(input("enter a no."))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for x in range(len(a)):
    if a[x] < no:
        b = a[x]
        print(b)

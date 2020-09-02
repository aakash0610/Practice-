name = str(input("Enter number:"))
x = name[::-1]


if x == name:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

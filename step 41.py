def main():
    value = int(input("enter a value: "))
    ten_percent(value)
    print("10 percent of", value, "is", ten_percent(value))

def ten_percent(num):
    return num*0.1

main()
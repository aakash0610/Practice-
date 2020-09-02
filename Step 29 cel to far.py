def convert_to_far(celsius):
    farenheit = celsius * 9/5 + 32
    return farenheit

c= int(input("what is temp: "))
f = convert_to_far(c)
print(f)
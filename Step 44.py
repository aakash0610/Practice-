
TUPLE = [54,76,32,14,29,12,64,97,50,86,43,12]


def main_menu():
    display = int(input(("1 – Display minimum \n2 – Display maximum \n3 – Display total \n4 – Display average \n5 – Quit"))
    ax = max(TUPLE)
    mini = min(TUPLE)
    tot = total(TUPLE)
    avg = vg(TUPLE)
    if display =='2':
        print (ax)
    elif display == '1':
        print(mini)
    elif display == '3':
        print(tot)
    elif display == '4':
        print(avg)
    elif display == '5':
        print("Goodbye and Thank you")
    else:
        print("invalid input")
        while display != 5:
        display = int(input(("1 – Display minimum \n2 – Display maximum \n3 – Display total \n4 – Display average \n5 – Quit"))



def max(TUPLE):
    TUPLE.sort()
    out1 = print("the largest number is: " + TUPLE[-1])
    return out1

def min(TUPLE):
    TUPLE.sort()
    out2 = print("the smallest number is: "+TUPLE[0])
    return out2

def total(TUPLE):
    tot = sum(TUPLE)
    return tot

def vg(TUPLE):
    vg = sum(TUPLE)/len(TUPLE)
    return vg


main_menu()

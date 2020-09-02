def main():
    vegetarian = str(input('Are you Vegetarian? (y/n)'))                                                                #take input from user
    veg = str(input('Are you Vegan? (y/n)'))                                                                            #take input from user
    glu = str(input('Are you Gluten free? (y/n)'))                                                                      #take input from user

    if vegetarian == "y" and veg == "y" and glu == "y":
        print('Here are your Restaurant choices: \n The Chef’s Kitchen or Corner Cafe')
    elif vegetarian == "y" and veg == "n" and glu == "n":
        print('Here are your Restaurant choices: \n Luigi’s Fine Italian Restaurant \n The Chef’s Kitchen or Corner '
              'Cafe \n Main Street Pizza – Vegetarian')
    elif vegetarian == "y" and veg == "n" and glu == "y":
        print('Here are your Restaurant choices: \n Main Street Pizza – Vegetarian ')
    elif vegetarian == "n" and veg == "n" and glu == "n":
        print('Here are your Restaurant choices: \n Joes’ Gourmet Burgers\n The Chef’s Kitchen or Corner Cafe\n Luigi’s Fine Italian Restaurant\n Main Street Pizza\n Corner Cafe')
    elif vegetarian == "n" and veg == "y" and glu == "n":
        print('Here are your Restaurant choices: \n Corner Cafe')
    elif vegetarian == "n" and veg == "n" and glu == "y":
        print('Here are your Restaurant choices: \n Main Street Pizza')
    else:
        print('Invalid Input')


main()

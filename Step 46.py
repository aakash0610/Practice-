import random


def main():
    states = {
        'Queensland': 'brisbane',
        'New South Wales': 'sydney',
        'South Australia': 'adelaide',
        'Western Australia': 'perth',
        'Victoria': 'melbourne',
        'Tasmania': 'hobart',
        'Northern Territory': 'darwin'
    }
    score = 0
    print('Lets play a game!')
    for i in range(6):
        state = random.choice(list(states.items()))
        answer = (input('the capital of ' + state[0] + ' is:'))
        if answer in state:
            score += 1
    print(score)


main()

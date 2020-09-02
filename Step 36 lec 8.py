import random
def question():
    print("welcome")
    finished = False
    while not finished:

        ques = str(input("Enter a question"))

        print(get_ans())

        play_again = input("would you like to play again? ").lower()
        finished = (play_again == 'no')
def get_ans():
    possible_ans = ['yes', 'no', 'idk', 'thats a stupid question']
    random_index = random.randint(0, 7)
    ran_ans = random.choice(possible_ans)
    return ran_ans

question()

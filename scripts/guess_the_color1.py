import random
#Guess the color on the rainbow#
def guesscolor1():
    ##While loop
    random_color = random.choice( ['red','blue','green','yellow','orange','purple'])
    guess = ""
    while guess != random_color:
        guess = str(input(f'\nGuess a color on a rainbow ').lower())
        if guess == "":
            print('\nPlease enter a color, answer cannot be blank ')
        elif guess != random_color:
            print('\nSorry you did not guess the correct color')
        elif guess == random_color:
            print('\nCongratulations, You selected the correct color!!!\n')

guesscolor1()


def guesscolor2():
    #For Loop
    random_color = random.choice( ['red','blue','green','yellow','orange','purple'])
    guess = ""
    for x in random_color:
        if guess != random_color:
            guess = str(input(f'\nGuess a color on a rainbow ').lower())
            if guess == "":
                print('\nPlease enter a color, answer cannot be blank ')
            elif guess != random_color:
                print('\nSorry you did not guess the correct color')
            elif guess == random_color:
                print('\nCongratulations, You selected the correct color!!!\n')
guesscolor2()
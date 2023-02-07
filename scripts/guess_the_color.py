import random

#Guess the color on the rainbow#

def guesscolor():
    random_color = random.choice( ['red','blue','green','yellow','orange','purple'])
    guess = ""
    while guess != random_color:
        guess = str(input(f'Guess a color on a rainbow ').lower())
        if guess == "":
            print('Please enter a color, answer cannot be blank ')
        elif guess != random_color:
            print('Sorry you did not guess the correct color')
        elif guess == random_color:
            print('Congratulations, You selected the correct color')

guesscolor()
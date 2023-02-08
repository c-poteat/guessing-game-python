import random

def guessnumber():
    randomnumber = random.randint(1,5)
    guess = 0
    while guess != randomnumber:
        try:
            guess = int(input(f'\nGuess a number between 1 to 5 '))
        except ValueError:
            print('\nEmpty input or not a number entered')
        if guess == randomnumber:
            print('\nCongratulations, You selected the correct number!!!\n')

guessnumber()
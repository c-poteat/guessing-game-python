import random

def guessnumber2():
    #For Loop
    lst = [1,2,3,4,5]
    guess = 0
    randomnumber = random.choice(lst)
    #Selected a range to 20 tries
    for i in range(0,20):
        randomnumber != random.choice(lst)
        try:
            guess = int(input(f'\nGuess a number between 1 to 5 '))
        except ValueError:
            print('\nEmpty input or not a number entered')
        if guess == randomnumber:
            print('\nCongratulations, You selected the correct number!!!\n')
            break 
        elif guess > 5:
            print('\nPlease enter a number that is less than 5')
guessnumber2()
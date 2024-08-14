#imports
import random
import time

r = random.Random()

#defines random computer guess for the rest of the program
computer_guess = r.randint(1, 100)

guess = print('''Hi user, I am thinking of a number between 1 and 100
and your job is to guess it.''')

time.sleep(1.5)

#User has not guessed the answer yet
guess_status = False

#Increments by 1 every time the user does not get it correct 
tries = 0

while guess_status != True:
    
    '''Input -> Some integer from 1-100
       Tells user whether there answer is correct or not
       outputs -> string'''
    
    guess = int(input("\nWhat is your guess: "))

    if guess < computer_guess:
        print(f'Sorry, {guess} is too low.')
        time.sleep(1)
        
    if guess > computer_guess:
        print(f'Sorry, {guess} is too high.')
        time.sleep(1)
    
    if guess == computer_guess:
        print(f'\n\nGreat job, {computer_guess} is correct!')
        guess_status = True #while loop ends
        time.sleep(1.2)
        
    tries += 1
    
print(f'\nIt took you {tries} tries.')

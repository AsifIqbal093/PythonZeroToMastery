"""Guessing Game."""

#importing random
import random

#generating a number from 1 to 10
num = random.randint(1, 10)



while True:
    try : 
        guess = int(input('Please enter a number between 1 to 10.'))
        if 0 < guess < 11:
            if guess == num :
                print('Yay! You got it :)')
                break
            else:
                print('Ooops! wrong guess!')
        else :
            print('Invalid Input, Try again!')
            continue
    except ValueError:
        print('Invalid Input, Try again!')

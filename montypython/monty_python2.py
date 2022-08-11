#!/usr/bin/env python3

# create counter
round = 0

# create while loop that will control program
while True:

    # increment counter
    round = round + 1

    # prompt user with questions and get input
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = input('Your guess --> ')

    # use if statemenrt to consider user input and act accordingly
    if answer == 'Brian':
        print('Correct!')
        break
    elif round == 3: 
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry! Try again!')



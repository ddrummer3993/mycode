#!/usr/bin/env python3
"""author: some guy at alta ptobably
    using this for a lab about loops and also pylint"""

# create counter
ROUND = 0

# create while loop that will control program
while True:

    # increment counter
    ROUND = ROUND + 1

    # prompt user with questions and get input
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = input('Your guess --> ')

    # use if statemenrt to consider user input and act accordingly
    if answer == 'Brian':
        print('Correct!')
        break
    if round == 3:
        print('Sorry, the answer was Brian.')
        break
    print('Sorry! Try again!')

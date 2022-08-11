#!/usr/bin/env python3
  
# create counter and answer variables
round = 0
answer = ' '

# create while loop that will control program
while round < 3 and answer != "Brian":

    # increment counter
    round = round + 1

    # prompt user with questions and get input
    answer = input('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = answer.capitalize()

    # use if statemenrt to consider user input and act accordingly
    if answer == 'Brian':
        print('Correct!')
    elif answer == 'Shrubbery':
        print('You gave the super secret answer!')
        break
    elif round == 3:
        print('Sorry, the answer was Brian.')
    else:
        print('Sorry! Try again!')


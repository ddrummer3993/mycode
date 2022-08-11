#!/usr/bin/env python3

# Welcome to the insult machine

# try again function
def try_again_clown():
    print("Not the brightest crayon in the box, are ya pal. Try again you clown.")
    main()

# main function
def main():

    # establish user input, a number 1-4
    inputNumber = float(input("pick a number 1-4: "))

    # use if statement logic to return an insult based off that number.
    if inputNumber == 4:
        print("yea you would pick the biggest number. compensating for something?")
    elif inputNumber == 3:
        print("Why not just go ahead an pick 4? you coward.")
    elif inputNumber == 2:
        print("you picked 2? HA. Your incredible lack of self confidence is showing.")
    elif inputNumber == 1:
        print("You're adopted. Yours parents dont really love you.")
    else:
        try_again_clown()

main()

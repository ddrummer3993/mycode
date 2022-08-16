#!/usr/bin/env python3
""" DDrummer | Amazon SDE apprentice - Python ILT
    Python class project: using a REST API to retreive and display requested search data. """

# imports
import requests
import time
import sys

# base API definition
API = 'https://rickandmortyapi.com/api'

# user input function
def prompt_user():
    search_method = input('Awh geez man, uh, how do you want to search the database? (character, location, episode, q to quit): ')
    
    # use logic statement to handle user search method input
    if search_method == 'character':
        print('searching by character')
    elif search_method == 'location':
        print('searching by location')
    elif search_method == 'episode':
        print('searching by episode')
    elif search_method == 'q':
        print('\nWay to be a quitter, JERRY.')
        sys.exit()
    else:
        print('\nCome on, Doofus Rick... I\'m sure you can get it right this time.\n')
        prompt_user()

# main function defintion
def main():
    """ main function of the program """

    # welcome line and prompt user for search method input, can search by character, location, or episode.
    print('Welcome to *BURP* search Rick and Morty. Let\'s go, in and out. 20 minutes adventure.\n')

    #after 2 seconds call the user input func
    time.sleep(2)
    prompt_user()

if __name__ == '__main__':
    main()


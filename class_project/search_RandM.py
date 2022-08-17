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
    search_method = input('Morty: Awh geez man, uh, how do you want to search the database? (character, location, episode, q to quit): ')
    
    # use logic statement to handle user search method input
    if search_method == 'character':
        character_search()
    elif search_method == 'location':
        location_search()
    elif search_method == 'episode':
        episode_search()
    elif search_method == 'q':
        print('\nRick: Way to be a quitter, JERRY.')
        sys.exit()
    else:
        print('\nRick: Thats not an option, Doofus Rick... I\'m sure you can get it right this time.\n')
        prompt_user()

# character search functions
def character_search():

    # prompt user to give a character name to search by
    character_name = input('\nMorty: alright man, uh, w-which character would you like to search for? ah geez: ')

    # create resp, our request object
    resp = requests.get(f'{API}/character/?name={character_name}')

    # .json() method converts JSON string into python data structure
    characters = resp.json().get('results')
    print(characters)

# location search function
def location_search():

    # prompt user to give a character name to search by
    location_name = input('\nMorty: Aw man ah geez, alright. i-is there a certain location you had in mind?: ')

    # create resp, our request object
    resp = requests.get(f'{API}/location/?name={location_name}')

    # .json() method converts JSON string into python data structure
    locations = resp.json().get('results')
    print(locations)

# episode search function
def episode_search():
    # prompt user to give a character name to search by
    episode_name = input('\nRick: Alright, bird brain. let\'s search for an episode, but see if you\'re smart enough to put it in the right format. First season number, than episode number (S01E01): ')

    # create resp, our request object
    resp = requests.get(f'{API}/episode/?episode={episode_name}')

    # .json() method converts JSON string into python data structure
    episode = resp.json().get('results')
    print(episode)

# main function defintion
def main():
    """ main function of the program """

    # welcome line and prompt user for search method input, can search by character, location, or episode.
    print('Rick: Welcome to *BURP* search Rick and Morty. Let\'s go, in and out. 20 minutes adventure.\n')

    #after 2 seconds call the user input func
    time.sleep(2)
    prompt_user()

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
""" DDrummer | Amazon SDE apprentice - Python ILT
    Python class project: using a REST API to retreive and display requested search data.
    This application will take user input and use it to retrieve relevant data from the
    Rick and Morty API and display it appropriately for the user. """

# imports
import time
import sys
import requests
import crayons

# base API definition
API = 'https://rickandmortyapi.com/api'

# define global variables
DATA_SEPERATOR = '\n================================================================'

# menu options function
def menu():
    """ creates and displays user menu """

    menu_opts = {'C':'character',
            'L':'location',
            'E':'episode',
            'Q':'quit'
            }

    # print out the menu options
    for opt in menu_opts.items():
        print(f'  - {opt[0]} for {opt[1]}')

# user input function
def prompt_user():
    """ prompts the user for unput to use for API search """

    while True:

        # grab user input for search method
        print('\nMorty: Awh geez man, uh, how do you want to search the database?')
        menu()
        search_method = input('\nSearch Method: ').upper()

        # use logic statement to handle user search method input
        if search_method == 'C':
            character_search()
        elif search_method == 'L':
            location_search()
        elif search_method == 'E':
            episode_search()
        elif search_method == 'Q':
            print('\nRick: Way to be a quitter, JERRY.')
            sys.exit()
        else:
            print('\nRick: Thats not an option, Doofus Rick... I\'m sure you \
can get it right this time.')
            prompt_user()

#  ---------------------------- character search funcs --------------------------------

# character search functions
def character_search():
    """ create character search API call """

    # prompt user to give a character name to search by
    character_name = input('\nMorty: alright man, uh, w-which character would \
you like to search for? ah geez: ')

    # create resp, our request object
    resp = requests.get(f'{API}/character/?name={character_name}')

    # .json() method converts JSON string into python data structure
    characters = resp.json().get('results')
    if characters:
        handle_char(characters)
    else:
        print('\nMorty: Gosh man, i dont think that character exists in the Rick \
and Morty universe...')
        character_search()

# handle character data response from R&M API
def handle_char(char_data):
    """ handles character search API call """

    print(f'{crayons.cyan(DATA_SEPERATOR)}')

    # loop through data and display key data for each character in the list
    for char in char_data:
        print(f'\nName: {char["name"]}')
        if char['status'] == 'Alive':
            print(f'\nStatus: {crayons.green(char["status"])} - {char["species"]}')
        elif char['status'] == 'Dead':
            print(f'\nStatus: {crayons.red(char["status"])} - {char["species"]}')
        else:
            print(f'\nStatus: {crayons.yellow(char["status"])} - {char["species"]}')
        print(f'\nOrigin location: {char["origin"]["name"]}')
        print(f'\nLast known location: {char["location"]["name"]}')
        print(f'{crayons.cyan(DATA_SEPERATOR)}')

#  ---------------------------- location search funcs --------------------------------

# location search function
def location_search():
    """ creat location search API call """

    # prompt user to give a character name to search by
    location_name = input('\nMorty: Aw man ah geez, alright. i-is there a \
certain location you had in mind?: ')

    # create resp, our request object
    resp = requests.get(f'{API}/location/?name={location_name}')

    # .json() method converts JSON string into python data structure
    locations = resp.json().get('results')
    if locations:
        handle_loc(locations)
    else:
        print('\nMorty: Gosh man, i dont think that location exists in the \
Rick and Morty universe...')
        location_search()

# handle location data response from R&M API
def handle_loc(loc_data):
    """ handles location search API call """
    print(f'{crayons.cyan(DATA_SEPERATOR)}')

    # loop through data and display key data for each character in the list
    for loc in loc_data:
        print(f'\nName: {loc["name"]}')
        print(f'\nType: {loc["type"]}')
        print(f'\nDimension: {loc["dimension"]}')
        print(f'{crayons.cyan(DATA_SEPERATOR)}')

#  ---------------------------- episode search funcs --------------------------------

# episode search function
def episode_search():
    """ create episode search API call """

    # prompt user to give a character name to search by
    print('\nRick: Alright, bird brain. let\'s search for an episode, but \
see if you\'re smart enough to put it in the right format.')
    episode_name = input('\nMorty: W-we need the season number first, then \
episode number, like this (S01E01): ')

    # create resp, our request object
    resp = requests.get(f'{API}/episode/?episode={episode_name}')

    # .json() method converts JSON string into python data structure
    episode = resp.json().get('results')
    if episode:
        handle_ep(episode)
    else:
        print('\nMorty: Gosh man, i dont think that episode exists in the \
Rick and Morty universe...')
        episode_search()

# handle episode data response from R&M API
def handle_ep(ep_data):
    """ hanldes episode search API call """

    print(f'{crayons.cyan(DATA_SEPERATOR)}')

    # loop through data and display key data for each episode
    for epsd in ep_data:
        print(f'\nName: {epsd["name"]}')
        print(f'\nAir Date: {epsd["air_date"]}')
        print(f'\nEpisode: {epsd["episode"]}')
        print(f'{crayons.cyan(DATA_SEPERATOR)}')

#  ---------------------------- MAIN FUNCTION --------------------------------

# main function defintion
def main():
    """ main function of the program """

    # welcome line and prompt user for search method input
    print('\nRick: Check it out MORTY. I\'m part of some python code...')
    print('IM PYTHON RIIIIIIIICK!')
    print('\nAnyway, Welcome to *BURP* search Rick and Morty. Let\'s go, in \
and out. 20 minutes adventure.')

    #after 2 seconds call the user input func
    time.sleep(2)
    prompt_user()

if __name__ == '__main__':
    main()

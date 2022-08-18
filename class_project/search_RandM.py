#!/usr/bin/env python3
""" DDrummer | Amazon SDE apprentice - Python ILT
    Python class project: using a REST API to retreive and display requested search data.
    This application will take user input and use it to retrieve relevant data from the 
    Rick and Morty API and display it appropriately for the user. """

# imports
import requests
import time
import sys
import crayons

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

""" ------------------ character search funcs ----------------------"""

# character search functions
def character_search():

    # prompt user to give a character name to search by
    character_name = input('\nMorty: alright man, uh, w-which character would you like to search for? ah geez: ')

    # create resp, our request object
    resp = requests.get(f'{API}/character/?name={character_name}')

    # .json() method converts JSON string into python data structure
    characters = resp.json().get('results')
    handle_char(characters)

# handle character data response from R&M API
def handle_char(charData):
    print('{}'.format(crayons.cyan('\n================================================================')))

    # loop through data and display key data for each character in the list
    for char in charData:
        print(f'\nName: {char["name"]}')
        if char['status'] == 'Alive':
            print(f'\nStatus: {crayons.green(char["status"])} - {char["species"]}')
        elif char['status'] == 'Dead':
            print(f'\nStatus: {crayons.red(char["status"])} - {char["species"]}')
        else:
            print(f'\nStatus: {crayons.yellow(char["status"])} - {char["species"]}')
        print(f'\nOrigin location: {char["origin"]["name"]}')
        print(f'\nLast known location: {char["location"]["name"]}')
        print('{}'.format(crayons.cyan('\n================================================================')))

""" ------------------ location search funcs ----------------------"""

# location search function
def location_search():

    # prompt user to give a character name to search by
    location_name = input('\nMorty: Aw man ah geez, alright. i-is there a certain location you had in mind?: ')

    # create resp, our request object
    resp = requests.get(f'{API}/location/?name={location_name}')

    # .json() method converts JSON string into python data structure
    locations = resp.json().get('results')
    handle_loc(locations)

# handle location data response from R&M API
def handle_loc(locData):
    print('{}'.format(crayons.cyan('\n================================================================')))

    # loop through data and display key data for each character in the list
    for loc in locData:
        print(f'\nName: {loc["name"]}')
        print(f'\nType: {loc["type"]}')
        print(f'\nDimension: {loc["dimension"]}')
        print('{}'.format(crayons.cyan('\n================================================================')))

""" ------------------- episode search funcs -----------------------"""

# episode search function
def episode_search():

    # prompt user to give a character name to search by
    episode_name = input('\nRick: Alright, bird brain. let\'s search for an episode, but see if you\'re smart enough to put it in the right format. First season number, then episode number (S01E01): ')

    # create resp, our request object
    resp = requests.get(f'{API}/episode/?episode={episode_name}')

    # .json() method converts JSON string into python data structure
    episode = resp.json().get('results')
    handle_ep(episode)

# handle episode data response from R&M API
def handle_ep(epData):
    print('{}'.format(crayons.cyan('\n================================================================')))

    # loop through data and display key data for each episode
    for ep in epData:
        print(f'\nName: {ep["name"]}')
        print(f'\nAir Date: {ep["air_date"]}')
        print(f'\nEpisode: {ep["episode"]}')
        print('{}'.format(crayons.cyan('\n================================================================')))

""" ------------------- MAIN FUNCTION -----------------------"""

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


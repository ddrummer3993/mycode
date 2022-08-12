#!/usr/bin/env python3

# import new code
import netifaces

# define ip adapter function
def adapterip(adaptername):
    return(netifaces.ifaddresses(adaptername)[netifaces.AF_INET][0]['addr'])

# define MAC adapter func
def adaptermac(adaptername):
    return(netifaces.ifaddresses(adaptername)[netifaces.AF_LINK][0]['addr'])

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print(adaptermac(i))
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        print(adapterip(i))
    except: 
        print('Could not collect adapter info')


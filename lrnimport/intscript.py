#!/usr/bin/env python3

# imports
from subprocess import call

# use call
call(['ip', 'link', 'show', 'up'])

print('This program will check your interfaces.')

# prompt user for interface and grab input
interface = input('Enter an interface, like, ens3: ')

call(['ip', 'addr', 'show', 'dev', interface])
call(["ip", "route", "show", "dev", interface])


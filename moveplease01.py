#!/usr/bin/env python3

# imports
import shutil
import os

def main():
    # force python program to start in the home user directory
    os.chdir('/home/student/mycode/')

    # move one file into a new folder with the other file
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt user for new name of the kerrigan.obj file
    xname = input('What is the new name for kerrigan.obj file? ')

    # "move" the kerrigan.obj into the exat some location, but rename it in doing so.
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()

#!/usr/bin/env python3

# create file object in read mode
configfile = open('vlanconfig.cfg','r')

# display file to the screed - .read()
print(configfile.read())

# close file and open file 
# configfile.close()
# configfile = open("vlanconfig.cfg", "r")
# OR use the .seek()
configfile.seek(0, 0)

# make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

# iterate through configlist
for x in configlist:
    print(x.strip(), end="")

# close file
configfile.close()


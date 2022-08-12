#!/usr/bin/python3

# create the counter
loginfail = 0

# open the file for reading
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')

# turn the files into a list of lines in memory
keystone_file_lines = keystone_file.readlines()

# loop through list of lines
for line in keystone_file_lines:

    # use if logic to check for specific condition, increase counter by one if found
    if '- - - - -] Authorization failed' in line:
        loginfail += 1 

print ('The number of failed login attempts is', loginfail)
keystone_file.close()


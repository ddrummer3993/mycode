
#!/bin/bash
#given a username and group name from the application user, adds a user to linux, assigns the user to a group, promptsif theyd like to add another.

# function gets user input, creates user, assigns to group
handleuser() {

    # adds user, adds group, and adds user to group
    sudo useradd $username
    sudo groupadd -f $groupname
    sudo usermod -aG $groupname $username

}

# starts our decision as yes
DECISION="Y"

# if our decision to add a user is Y, then we get user info and call the handleuser function
while [ $DECISION == "Y" ]
do
     # grab username from user
    echo "Enter the name of your new user:"
    read username

    # grab groupname form user
    echo "next, enter the group you'd like this user to be in:"
    read groupname

    # call handle user function
    handleuser

    # prompt user to add another user
    echo "Would you like to enter a new user? (Y/N)"
    read DECISION
done



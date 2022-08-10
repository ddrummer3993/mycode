#!usr/bin/env python3

# create a list contianing three items
my_list = [ "192.168.0.5", 5060, "UP"]

# dispaly the first item on the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item on the list
print("The second item on the list (port): " + str(my_list[1]) )

# display the last item on the list
print("The last item on the list (state): " + my_list[2] )

# another list of IP info
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(f"The IP addresses in iplist are: {iplist[3]} and {iplist[4]}")



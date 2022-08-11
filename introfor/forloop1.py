#!/usr/bin/env python3

# create list called vendors
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista']
approved_vendors = ['cisco', 'juniper', 'big_ip']

# loop across vendors
for x in vendors:
    print('\nthe vendor is: ' + x, end="")
    if x not in approved_vendors:
        print(' - NOT AN APPROVED VENDOR!', end="")

print('\nOur loop has ended.')

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for x in farms:
    for key, value in x.items():
        print(f"{key}: {value}")






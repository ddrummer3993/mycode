#!/usr/bin/env python3

# create 3 lists, one of favorite snacks, one of favorite meals, one of favorite desserts
favSnacks = [ "trail-mix", "greek yogurt", "cliff bars", "chips" ]
favMeals = [ "cheeseburger", "steak", "moms meatloaf", "pasta" ]
favDesserts = [ "ice cream", "cookies", "cheesecake" ]

# create empty list of favorite foods and append all three ofrmer lists
favFoods = []
favFoods.append(favSnacks)
favFoods.append(favMeals)
favFoods.append(favDesserts)

# display favFoods list which is a list of lists.
print(favFoods)
print("My favorite food is: " + favFoods[1][0] )

# make dictionary of superheros
wolverine = {"Real Name": "James Logan Howlett",
             "Team": "X-men",
             "universe": "Marvel",
             "SuperPower": [ "accelerated healing", "retractable claws", "animal-like senses" ]
             }

superman = {"Real Name": "Clark Kent",
             "Team": "Justice League",
             "Universe": "DC",
             "SuperPower": [ "super strength", "incredible strength", "impervious skin" ]
             }

ironMan = {"Real Name": "Tony Stark",
           "Team": "Avengers",
           "Universe": "Marvel",
           "SuperPower": [ "genius", "superhuman armor" ]
            }

print(wolverine)
print(wolverine.keys())
print(wolverine.values())



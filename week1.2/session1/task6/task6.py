# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

artists = {

    "J Cole": [
        ("The Fall-Off", 2025),
        ("Might Delete Later", 2024),
        ("4 Your Eyez Only", 2016),
        ("2014 Forest Hills Drive", 2014),
        ("The Off-Season", 2021)
    ],

    "Kendrick Lamar": [
        ("good kid, m.A.A.d city", 2012),
        ("To Pimp a Butterfly", 2015),
        ("DAMN.", 2017),
        ("Mr. Morale & the Big Steppers", 2022),
        ("GNX", 2024)
    ],

    "Kanye West": [
        ("The College Dropout", 2004),
        ("Late Registration", 2005),
        ("My Beautiful Dark Twisted Fantasy", 2010),
        ("Yeezus", 2013),
        ("The Life of Pablo", 2016)
    ],

    "Westside Gunn": [
        ("Pray for Paris", 2020),
        ("Flygod", 2016),
        ("HWH 8: Side A", 2021),
        ("And Then You Pray for Me", 2023)
    ],

    "Freddie Gibbs": [
        ("Piñata", 2014),
        ("Bandana", 2019),
        ("Alfredo", 2020),
        ("Alfredo 2", 2025),
        ("You Only Die 1nce", 2025)
    ],

}

# Pretty-print the data structure

pprint(artists)

# Display details of one album recorded by a specific artist

item = artists["J Cole"][2]
name, year = item[0], item[1]
print(f"Name of album: {name}.\nYear of release: {year}.")
# \n isn't working with pprint() for me.

# Calculating number of albums in the dictionary
count = 0

for value in artists.values():
    count += len(value)

print(f"Number of albums in the database: {count}")
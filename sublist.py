"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 0
UNEQUAL = 3

def check(smaller, bigger):
    sml = len(smaller)
    big = len(bigger)
    
    for i in range(big - sml + 1):
        if smaller == bigger[i:i+sml]:
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif len(list_one) > len(list_two):
        if len(list_two) == 0:
            return SUPERLIST
        elif(check(list_two, list_one)):
            return SUPERLIST
    else:
        if len(list_one) == 0:
            return SUBLIST
        elif (check(list_one, list_two)):
            return SUBLIST
    return UNEQUAL
    

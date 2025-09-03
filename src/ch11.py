# Sets

# 1  Sets
# Complete the remove_duplicates function. It should take a list of spells that a player has learned and return a new List where there is at most one of each title. You can accomplish this in at least two ways:
# create a second list and if the spell isn't in the list, add it, then sort it (optional use a set)

def remove_duplicates(spells:list):
    condensed_spells = set(spells)
    new_spell_list = sorted(list(condensed_spells))
    return new_spell_list

# 2 Vowels 
# Complete the count_vowels function. It takes a string and returns:

# The number of vowels in the string
# A set of the unique vowels found in the string

def count_vowels(text:str):
    vowels_def = "aeiouAEIOU"
    vowels_used = set()
    count = 0
    for char in text:
        if char in vowels_def:
            vowels_used.add(char)
            count += 1
    return count, vowels_used

# Set Subtraction
# Complete the find_missing_ids function. It accepts two lists as input, and returns a new set of all the IDs that are in the first list but are not in the second.

# Naturally, there will be no duplicates in the resulting set.

def find_missing_ids(first_ids:list, second_ids:list):
    return set(first_ids) - set(second_ids)


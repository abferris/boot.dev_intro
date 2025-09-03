# Chapter 9 Lists

# 1 Lists
# Let's work on Fantasy Quest's inventory! We can store items the player is carrying in a list! # Fix our get_inventory function by adding Shortsword to the end of the list.

def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Short Sword"]

# 2 Indexing Into Lists

# We need to allow our players to access items in their inventories!
# Fix our get_leather_scraps function by changing the value of item_index(0) to the index in inventory that holds the value "Leather Scraps".
def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]
    item_index = 1
    return inventory[item_index]

# 3 List Length

# Some of our player's inventories are huge, so looking through the entire list is cumbersome. Let's find an easy way for us to get the index of the last item in their inventory.

# Complete the get_last_index function so that it returns the length of the inventory list minus 1.

def get_last_index(inventory):
    return len(inventory) - 1

# 4 List Updates
# Fantasy Quest is trialing a new inventory system for their hardcore game mode. If a player has Iron Ore or an Iron Bar, it is always stored in the 2nd inventory slot (and they can only have one or the other).
# Let's finish the smelt_ore function:

# Check if they have Iron Ore in the second inventory slot.
# If they do, change it into an Iron Bar.

def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory

# 5 Appending in Python

# We need to generate a unique user ID for each player in the game. An ID is just a unique number that identifies a user.

# Let's finish the generate_user_list function. In the body of the loop, use the incrementing value i as unique IDs and append them to the player_ids list.

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids

# 6 Pop Values

# Our player is selling the items in their inventory to the shopkeep!
# Pop the last element from the inventory list until there is nothing left. Pop the elements into an item variable so that each prints in turn on line 19.

def clear_inventory(inventory):


    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")

# 7 Counting the Items in a List
# Assignment
# Our players need a way to see how many copies of a specific item they have within their inventory!

# Let's finish the get_item_counts function.

# Within the loop, check if the items are a Potion, Bread, or Shortsword.
# If you find a match, increment the corresponding counter, either potion_count, bread_count or shortsword_count.

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1
    # don't touch below this line

    return potion_count, bread_count, shortsword_count

# 8 Find an Item in a List
# Assignment
# We need to check if a player has a specific item in their inventory. In the contains_leather_scraps function, use the no-index syntax to iterate over each item in items. If you find an item called Leather Scraps, set the found variable to True.

def contains_leather_scraps(items):

    for item in items:
        if item == "Leather Scraps":
            return True
    return False

# 10 Find the Increase

# Complete the loop inside check_character_levels. It already loops over all of the indexes i in old_character_levels. The old_character_levels and new_character_levels lists are the same length, which means you can use i to index into both.
# For each iteration, use i with bracket notation to get the items at the same index from both lists.
# Check if the level in old_character_levels is less than the level in the new_character_levels.
# If so, print i. (Do not print anything if they didn't level up or somehow leveled down.)
# changing to take old_chars and new_chars (as an array of levels).

def check_character_levels(old_chars:list, new_chars:list):
    for i in range(0, len(old_chars)):
        if new_chars[i] > old_chars[i]:
            print(f"Player {i} Leveled up")

# 11 Find Max

# Complete the find_max function that looks at each number in the nums list and returns the maximum value. If no maximum is found, it just returns negative infinity. I've added it for you as the starting value of max_so_far.


def find_max(nums:list):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far

# 12 Modulo Operator in Python
# Inside the loop in the get_odd_numbers function, use the modulo operator to check if each number, i, is odd. If a number is odd, append it to the odd_numbers list. The function already returns the odd_numbers list for you. num is an integer.

def get_odd_numbers(num:int):
    odd_numbers = []

    for i in range(0, num):
        if i % 2 == 1:
         odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers

# 13 Slicing Lists

# Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:

# First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
# Next, return a slice of the champions list that starts at the beginning of the list and includes all champions except for the very last champion.
# Last, return a slice of the champions list that only includes the champions in even numbered indexes.

def get_champion_slices(champions:list):
    output1 = champions[2:]
    output2 = champions[0:-1]
    output3 = champions[::2]
    return output1,output2,output3

# 14 List Operations - Concatenate
# Create a new list that combines the lists favorite_weapons, favorite_armor, and favorite_items in this order.
# Return the list containing the combined favorites.

def concatenate_favorites(favorite_weapons:list, favorite_armor:list, favorite_items:list):
    return favorite_weapons + favorite_armor + favorite_items

# 15 List Operations - Contains
# Complete the is_top_weapon function. It should return True if the weapon is in the top_weapons list, otherwise it should return False.

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    # don't touch above this line

    return weapon in top_weapons

# 16 List Deletion
# In Fantasy Quest there is a list of strongholds on the map that players can visit to defeat powerful bosses. Let's update the trim_strongholds function to:

# Delete the first stronghold from the list
# Delete the last two strongholds from the list

def trim_strongholds(strongholds):
    del strongholds[0:1]
    del strongholds[-2:]
    return strongholds

# 17 Tuple Unpacking
# example: wronglist = ["Glorfindel", 2093, True, "Gandalf", 1054, False, "Gimli", 389, False, "Aragorn", 87, False,]
# Restructure the heroes list into a list of tuples by editing the syntax, where each tuple represents one hero and contains their data in the same order.

def get_heroes(heroes):
    go = True
    current = 0
    while current < len(heroes):
        hero =  (heroes[current], heroes[current+1],heroes[current+2])
        heroes[current] = hero
        del heroes[current+1]
        del heroes[current+1]
        current += 1
    return heroes

# 18 first element
# Let's add another function to our inventory system. Write a function that returns the first element from a list. If the list is empty then return the string ERROR instead.

def get_first_item(items):
    return "ERROR" if len(items) == 0 else items[0]

# 19 Reverse List
# Some of our players would like to view their inventories in reverse order.
# Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

def reverse_list(items):
    output = []
    for i in range(len(items), 0, -1):
        output.append(items[i-1])
    return output

# 20 Filter Messages
# A list of the same messages but with all instances of the word dang removed.
# A list containing the number of dang words that were removed from each message at that particular index.
def filter_messages(messages):
    output = []
    counts = []
    for message in messages:
        words = message.split()
        count = 0
        i = 0
        while i < len(words):
            if words[i] == "dang":
                count += 1
                del words[i]
            else:
                i += 1
        output.append(" ".join(words))
        counts.append(count)
    return output, counts

# 21 Even Teams
# Complete the split_players_into_teams function.

# It accepts a list of players (strings representing their names) and returns two lists in this order:

# A new list of all the players with even-numbered indexes in the original list.
# A new list of all the players with odd-numbered indexes in the original list.
def split_players_into_teams(players):
    return players[::2], players[1::2]


# 22 Alchemy Ingredients

# Complete the check_ingredient_match function. It accepts two lists of strings:

# recipe: The list of ingredients needed.
# ingredients: The list of ingredients the character has.
# It should return two values:

# A float representing the percentage of required ingredients the character has.
# A new list of ingredients the character is missing but that are required.
# Assume that the recipe list won't contain any duplicates (recipes require only one ingredient of each kind).

def check_ingredient_match(recipe, ingredients):
    missing = [item for item in recipe if item not in ingredients]
    percent = 100 * (1 - len(missing)/len(recipe))
    return percent, missing




# Chapter 12: Errors

# 1: Errors and Exceptions in Python


# One of the calls to get_player_record is raising a player id not found exception. Change the code in the main function to safely make all four calls within one try-except block. If an exception is raised, print the exception instead.

def level_one_main():
    try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
    except Exception as e:
        print(f"An unexpected error has occured: {e}")


# Don't edit below this line


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")

# 2 Raising your own exceptions
# If a player_id that doesn't exist is passed into the get_player_record function, we need to raise (but not handle) our own error to alert the caller of our function that the player they are looking for doesn't exist. The exception should say player id not found.

def get_player_record(player_id):
    try:
        if player_id == 1:
            return {"name": "Slayer", "level": 128}
        if player_id == 2:
            return {"name": "Dorgoth", "level": 300}
        if player_id == 3:
            return {"name": "Saruman", "level": 4000}
        raise Exception("Nonexistent player ID!")
    
# 3 Different Types of Exceptions
# Take a look at the get_player_record function. It raises an exception for negative player_ids.

# Complete the process_player_record() function so that it:

# Calls get_player_record(player_id) and returns its result if no error occurs.
# If an IndexError is raised, returns the string: index is too high.
# If any other exception happens, returns the error object itself. 
def process_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e

# Don't edit below this line

def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]

# 4 Purchase Bug

# Complete the purchase_item function.

# If the character doesn't have enough gold raise an Exception with the text not enough gold.
# Otherwise, return the amount of remaining money the customer has after completing the purchase.

def purchase_item(price, gold_available):
    if price > gold_available:
        raise Exception("not enough gold")
    else
        return gold_available - price

# Dictionaries 

# 1 Dictionary
# Complete the get_character_record function. It takes a character's name, server, level, and rank as individual inputs, and returns a dictionary with the following string keys:

# "name"
# "server"
# "level"
# "rank"
# "id"

def get_character_record(name, server, level, rank):
    char = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }
    return char

# 2 Duplicate Keys

    # fix this 
    # def get_character_record(name, server, level, rank):
    # return {
    #     "name": name,
    #     "server": server,
    #     "level": level,
    #     "level": 1,
    #     "rank": rank,
    #     "rank": 2,
    #     "id": f"{name}#{server}",
    # }
def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }

# 3 Counting practice 

# We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind. Fix the count_enemies function. It accepts as input:

# enemy_names: a list of strings.
# It should return a dictionary where:

# The keys are all the enemy names from the list
# The values are the counts of how many times each enemy appeared in the list.
# Run the code in its current state. It will raise a KeyError.
# Fix the code.

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name not in enemies_dict:
            enemies_dict[enemy_name] = 1
        else:
            enemies_dict[enemy_name] += 1
    return enemies_dict

# 4 Iterating Over a Dictionary in Python

# Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count.
# If there are no enemies, return the Python None value (not a string). If there are multiple enemies with the same highest count, return the first one found.

def get_most_common_enemy(enemies_dict:dict):
    output = None
    largest = float("-inf")
    for name in enemies_dict:
        amount = enemies_dict[name]
        if amount > largest:
            largest = amount
            output = name
    return output

# 5 Quest Status
kaladin_progress = {
    "entity": {
        "character": {
            "name": "Kaladin",
            "quests": {
                "bridge_run": {
                    "status": "In Progress",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        }
    }
}
# Complete the get_quest_status function. It accepts a progress dictionary (structure defined above) and returns the character's status in the "bridge_run" quest.
def get_quest_status(progress):
    return progress["entity"]["character"]["quests"]["bridge_run"]["status"]

# 6 Merge Dictionaries

# Complete the merge function. It accepts two dictionaries as input and returns a new merged dictionary that contains all the keys and values from the input dictionaries.

# There are multiple solutions that use built-in Python functions, but we'll use loops for practice:

# Create an empty dictionary to hold the new merged result
# Iterate over the key/value pairs of dict1 and add them to the merged dictionary
# Iterate over the key/value pairs of dict2 and add them to the merged dictionary
# Return the newly merged dictionary
# If a key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary.

def merge(dict1, dict2):
    newdict = dict1.copy()
    for char in dict2:
        newdict[char] = dict2[char]
    return newdict
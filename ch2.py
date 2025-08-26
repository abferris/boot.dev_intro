# Some of these will be changed into return values.
# Chapter 2 Variables

# 1 introducing how to use variables
def return_variable(player_health):
    return player_health

# 2 mutibility
def four_hits(player_health,damage):
    player_health -= damage
    print(player_health)

    player_health -= damage
    print(player_health)

    player_health -= damage
    print(player_health)

    player_health -= damage
    print(player_health)

# 3 Storing results
def armor_calc(player_health, armor_multiplier):
    armored_health = player_health*armor_multiplier
    return armored_health

# 4 Negative Numbers
def psn_damage(player_health):
    poison_damage = -10
    player_poison_health = player_health + poison_damage
    return player_poison_health

# 5 comments
def ideal_weapon(weapon):
    #the best_sword variable holds the value of the best sword in the game
    best_weapon = "Perfect " + weapon
    return best_weapon

# 6 Variable Types 
def define_types(val):
    return type(val).__name__

# 7 F-Strings in Python
def player_information(name, age, race):
    return f"{name} is a {race} who is {age} years old."

# 8  NoneType Variables and comparison
def reset_enemy():
    enemy = None
    return (enemy is None)

# 9 Adding Strings
def health_message(name: str):
    return name + " has a max health of 1200"

#10 Boots: this bit is more about the platform than anything
def quest_messages():
    quest_start = "You there! Adventurer!"
    quest_middle = "The local mine has been taken over by orcs!"
    quest_end = "We need your help taking it back."
    quest_objective = "Bring back 8 of their axes as proof of your hard work."
    space = " "

    print(quest_start)
    print(quest_middle)
    print(quest_end + space + quest_objective)

#11 Spellbook: round function

def avg_score(*args:int):
    average_score = (sum(args))/len(args)
    return round(average_score)

#12 Character Report: This is a compilation of everything here

def char_rep(name:str, level, char_class:str, magic_res,active):
    print("Character Report")
    print(f"{name} is a level {level} {char_class}.")
    print(f"They have {magic_res} magic resistance.")
    print(f"Their account is currently active: {active}")

    print("=========================")
    print("Character Report Complete")
    print("Data types:")
    print(
        f"name: {type(name).__name__}, level: {type(level).__name__}, char_class: {type(char_class).__name__}"
    )
    print(f"magic_resistance: {type(magic_res).__name__}")
    print(f"account_active: {type(active).__name__}")
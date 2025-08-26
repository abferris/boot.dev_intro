# Chapter 7: Comparisons

# 1 Comparison Operator

def player_1_wins(player_1_score: int, player_2_score: int):
    # Complete the player_1_wins function. It should return True if player 1 has a higher score, and False otherwise.
    return True if player_1_score > player_2_score else False

# 2 Comparison Operator Evaluations: just putting the operators will return true or false based off what is there


def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    # Create the following variables. Use comparison operators to determine their boolean values. The context of the parameter names should tell you how to make these comparisons. Return them in this order:
    is_mustang_edward_same = edward_height == mustang_height
    is_alphonse_edward_same = edward_height == alphonse_height
    is_winry_alphonse_same = edward_height == winry_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same

# 3 Comparison Practice

def can_withstand_blow(hero_armor, enemy_damage):
    # Complete the can_withstand_blow function. It should return True if the hero's armor is greater than or equal to the damage dealt by the enemy, and False otherwise.
    return hero_armor >= enemy_damage

# 4 If Statements

def print_status(player_health):
    # Complete the print_status function.
    # If player_health is less than or equal to 0, print the text dead to the console.
    # Afterwards, whether or not the player is dead, print the text status check complete to the console.
    if player_health > 0:
        print('Dead')
    else :
        print("Alive")
    print('status check complete')

# 5 If Practice

def check_swords_for_army(number_of_swords, number_of_soldiers):
    # Complete the check_swords_for_army function. If the number of swords and the number of soldiers match, return the string: "correct amount"
    # Otherwise, return the string: "incorrect amount"
    if number_of_swords == number_of_soldiers :
        return 'correct amount'
    return 'incorrect amount'

# 6 If Else

def player_status(health):
    # Complete the player_status function. If the player's health is less than or equal to 0, return the string: 'dead' Otherwise, if it's less than or equal to 5 return the string: 'injured' Otherwise, return the string: 'healthy'
    if health <= 0:
        return 'dead'
    elif health < 5:
        return 'injured'
    return 'healthy'

# 7 If-Else Practice

def check_high_score(current_player_name, high_scoring_player_name):
    if current_health == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"

# 8 If-Else Practice

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    # Complete the check_high_score function. If the player_name matches the high score name, return the string: "high" Otherwise, if it's the low scorer, return the string: "low". Otherwise, return the string: "neither"
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    return "neither"

# 9 Boolean Logic

# We need a way for our game to track whether a character's attack hits or misses.

# Complete the does_attack_hit function. The function should return True if either of the following conditions are met:

# The attack_roll is not a 1 and the attack roll is greater than or equal to the armor_class, or
# The attack roll is a 20
# Otherwise, it should return False.
# i added modifier field

def does_attack_hit(attack_roll, armor_class, mod=0):
    total = attack_roll+mod
    return attack_roll != 1 and total >= armor_class or attack_roll == 20

# 10 Should Serve Drinks
# In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

# Complete the function that determines if a bartender should serve drinks to a customer. Only return True if all of these conditions apply. If any of these conditions are False, return False:

# The customer's age is 21 or older
# The bartender is working
# The time is between 5 and 10 o'clock (inclusive). assuming integer 0-12

def should_serve_customer(customer_age:int, on_break:bool, time):
    is_open time =< 10 and time >= 5
    return  not on_break and customer_age >=21 and  is_open

# 11 Mount Rental

# Complete the check_mount_rental function. It takes two inputs:

# time_used - the amount of time the mount has been used in minutes
# time_purchased - the amount of time the character rented the mount for
# If time_used meets or exceeds time_purchased, then the rental is expired and greedy Uper will charge a fee, so the function should return the string "overtime charged"
# Otherwise, return the string "no charges yet"

def mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    else:
        return "no charges yet"

# 12 Combat Advantage

# On line 4 write an if/elif/else block. Using the rules specified above, set advantage, disadvantage, or evenly_matched to True depending on the values of player_power and enemy_defense.
# For example, if the player's power is greater than the enemy's defense, advantage should be set to True. etc.

def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True

    return advantage, disadvantage, evenly_matched
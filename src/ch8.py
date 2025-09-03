# Chapter 8: Loops

# 1 Loops
# Complete the missing sections of the for-loop in the print_numbers function so that it prints the numbers 0-99 to the console.

def print_numbers():
    for i in range(0,99):
        print(i)

# 2 Loops Practice
# In the print_numbers function, write a for-loop from scratch that logs the numbers 0-199 to the console.

def print_numbers_two():
    for i in range(0,199):
        print(i)

# 3 Loops Practice Two: For loops starting not at zero
#print from 5 to end value.

def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)

# 4 Range Contiunued
# Fix the for loop in the count_down function. It takes start and end inputs, but start is always greater than end. It's supposed to print numbers counting down from start to end, exclusive, but there's a mistake in the range function call.

def count_down(start, end):
    for i in range(start, end, -1):
        print(i)

# 5 Sum Game

# Fix the bug in the sum_of_numbers function. Instead of adding 1 to total at each iteration of the loop, it should add i. For example, instead of: 1 + 1 + 1 + 1 + 1... we want: 0 + 1 + 2 + 3 + 4...

# The desired output is a single number after the loop has finished executing.

def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

# 6 Sum Game 2

# add odd numbers

def sum_of_odd_numbers(end):
    total = 0
    for i in range(0, end):
        if i % 2 != 0 :
            total += i
    return total

# 7 While
# Complete the regenerate function using a while loop. It takes current_health, max_health and enemy_distance integers and returns an integer.

# Use a while loop to determine if they can regenerate. Assume they're stationary and enemies are pursuing them.
# If the character's current_health is less than their max_health, they can regenerate.
# If an enemy is more than a distance of 3 from the character, then the character can regenerate health.
# For each iteration of the loop:
# The character gains 1 health.
# The enemy_distance shortens by 2.
# Return the new current_health after regeneration stops.

def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2

    return  current_health

# 8 Match Countdown
# Complete the countdown_to_start function.

# Write a loop that counts down from 10 to 1. At each iteration, print the number with an ellipsis:
# However, when i is 1, print "Fight!" additionally:

def countdown_to_start():
    i = 10
    print("Counting down to match start:")
    while i > 1 :
        print(f"{i}...")
        i -= 1
    print(f"{i}... Fight!")

# 9 Experience Points
# Complete the calculate_experience_points function.
# It accepts a level (integer) and returns the total XP a player has gained so far.

def calculate_experience_points(level):
    i = 1
    output = 0
    while i < level:
        output += i*5
        i+=1
    return output


# 10 Meditate
# Complete the meditate function using a while loop. It accepts:

# mana: the current mana of the character.
# max_mana: the maximum mana of the character.
# num_potions: the number of mana potions the character has.
# It consumes potions one at a time until either:

# The character's mana has reached its maximum
# The character has no more potions left
# Each potion restores 1 point of mana.

# When the meditation is over, it returns the player's mana and the number of potions left, in that order.

def meditate(mana, max_mana, num_potions):
    meditation = True
    while meditation:
        if mana == max_mana or num_potions == 0:
            meditation = False
        else :
            num_potions -= 1
            mana += 1
    return [mana, num_potions]
 
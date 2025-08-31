# Chapter 3: Functions

#1 functions
def attack_area(weapon_name,rad):
    #provided functions/variables
    def area_of_circle(radius):
        pi = 3.14
        area = pi * radius * radius
        return area

    sword_length = 1.0
    spear_length = 2.0
    # Define sword area and spear area
    wep_area = area_of_circle(rad)
    #provided returns
    print(f"{weapon_name} length: {rad} meters.")
    print(f"{weapon_name} attack area: {wep_area} square meters.")

#2 Multiple parameters

def print_triple_attack(attack_one, attack_two, attack_three):
    
    # write triple attack function 
    
    def triple_attack(first:int, second:int, third:int):
        return( sum([first,second,third]))

    # provided variables and returns

    first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

    print("Attacking for", attack_one, attack_two, "and", attack_three, "...")
    print(first_triple_attack_damage, "points of damage dealt!")
    print("=====================================")

#3 Printing vs Returning
def char_report(first,last,occupation):
    #define get_title function
    def get_title(first_name, last_name, job):
        title = first_name + " " + last_name + " the " + job
        return title

    def report(first_name, last_name, job):
        print("First name:", first_name)
        print("Last name:", last_name)
        print("Job:", job)
        print("Title:", get_title(first_name, last_name, job))
        print("=====================================")

    return report(first,last,occupation)

#4 where to declare functions: teraching that order matters
def bootup_message():
    def main():
        print("Fantasy Quest is booting up...")
        print("Game is running!")

    return main()

#5 Community: trying to teach about their discord

def farenheight_to_celcius(deg):
    def to_celsius(f):
        return 5/9 * (f - 32)

    c = round(to_celsius(deg), 2)
    return f"{deg} degrees fahrenheit is {c} degrees celsius"

#6 Solutions: trying to teach about boot.dev exp mechanics
def hours_seconds_conversion(hrs):
    def hours_to_seconds(hours):
        return hours * 3600
    # Don't touch below this line
    secs = hours_to_seconds(hrs)
    return f"{hrs} hours is {secs} seconds"

#7 Return Multiple Values
def return_warrior(name, power): 
    def become_warrior(full_name, start_power):
        title = full_name + " the warrior"
        new_power = start_power+1
        return title, new_power
    
    # Don't edit below this line

    def main():
        test("Frodo Baggins", 5)
        test("Bilbo Baggins", 10)
        test("Gandalf The Grey", 9000)

    result1, result2 = become_warrior(name, power)
    return f"{result1} has a power level of {result2}"


    main()

# 8 Default Values 
def test_damage(health,armor):
    def get_punched(health, armor=0):
        damage = 50 - armor
        new_health = health - damage
        return new_health

    def get_slashed(health, armor=0):
        damage = 100 - armor
        new_health = health - damage
        return new_health

    # Don't touch below this line

    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")

# 9 Curse

def curse_options(damage):
    def curse(weapon_damage):
        lesser_cursed = weapon_damage * .5
        greater_cursed = weapon_damage * .25
        return lesser_cursed, greater_cursed
    
    # Don't modify below this line
    print("Weapon's base damage:", float(damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")

# Enchant and Attack

def enchant_attack(target_health,damage,weapon):
    
    def enchant_and_attack(health,dmg,wep):
        new_weapon = "enchanted " + wep
        new_weapon_damage = dmg + 10
        damaged_health = target_health - new_weapon_damage
        return new_weapon, damaged_health

    print(f"The target has {target_health} health.")
    print(f"{weapon} base damage: {damage}... Enchanting and attacking.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"The target has been attacked with the {enchanted_weapon}.")
    print(f"The target has {new_health} health remaining.")
    print("=====================================")
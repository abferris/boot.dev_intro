#Ch5 Unit Tests

# 1 Unit Tests: teaching user how to check their unit tests on boot.dev platform
def total_xp(level,xp_to_add):
    return level*10+xp_to_add

# 2 Debugging: Teaching users how to log things and run them to figure out what you're doing
def take_magic_damage(health, resist, amp, spell_power):  
    amp_spell_damage = amp * spell_power
    final_damage = amp_spell_damage - resist
    new_health = health - final_damage
    return new_health

# 3 Debugging Practice: learning to read errors and placeholder nones
def unlock_achievement(before_xp, ach_xp, ach_name):
    #function should return the new xp after recieving the achievement and "Achievement Unlocked: __achievement_name__"
    new_exp = before_xp + ach_xp
    alert = "Achievement Unlocked: " + ach_name
    return new_exp, alert

#4 Stack Trace: Teaching users how to look at a debugger to see where errors are
def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg

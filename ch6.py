#Chapter 6: Computing

# 1 Python numbers - Teaching the difference between an integer and a float

def calculate_damage(sword, arrow, spear, dagger, fireball):
    # Complete the missing sections of the calculate_damage function.
    # Fix the total_damage variable so that it contains the sum of all the different weapons' and spells' damage values.
    # Fix the average_damage variable so that it contains the average of the combined weapon and spell damage.
    total_damage = sum([sword,arrow,spear,dagger,fireball])
    average_damage = total_damage/5
    return total_damage, average_damage

# 2 Changing in place
def update_player_score(current_score, increment):
    # Complete the update_player_score function. It should add increment to current_score and then return the new current_score.
    current_score += increment
    return current_score

# 3 Plus Equals
def get_hurt(current_health, damage):
    # Complete the get_hurt function. It should use the -= in-place operator to subtract damage from current_health and then return the new current_health.
    current_health -= damage
    return current_health

# 4 Scientific notation
def max_players_on_server():
    return 1.0244e18,1.0244e19,1.0244e20
    # Complete the max_players_on_server function. It takes no inputs, but simply returns 3 static numbers:
    # The max players on a "small" server: 1,024,000,000,000,000,000 (1.024e18)
    # The max players on a "medium" server: 10,240,000,000,000,000,000
    # The max players on a "large" server: 102,400,000,000,000,000,000

# 5 Bitwise "&" Operator
def perm_bits(perms):
    # Task is to return whether the inputted perms has each permission.
    can_create_guild = 0b1000
    can_review_guild = 0b0100
    can_delete_guild = 0b0010
    can_edit_guild =   0b0001
    
    def get_create_bits(user_permissions):
        return False if user_permissions & can_create_guild == 0 else True


    def get_review_bits(user_permissions):
        return False if user_permissions & can_review_guild == 0 else True


    def get_delete_bits(user_permissions):
        return False if user_permissions & can_delete_guild == 0 else True


    def get_edit_bits(user_permissions):
        return False if  user_permissions & can_edit_guild == 0 else True

    return get_create_bits(perms), get_review_bits(perms), get_delete_bits(perms), get_edit_bits(perms)

# 6 Bitwise | Operator

def calculate_guild_perms(*users):
    # A "guild" is a team of 2-4 players. Here are the guild-specific permissions:

    # can_invite - Leftmost bit (0b1000)
    # can_kick - Second to leftmost bit (0b0100)
    # can_enter_dungeon - Second to rightmost bit (0b0010)
    # can_surrender - Rightmost bit (0b0001)
    # When players are in a guild together, they gain all the permissions of all the other members of the guild!
    # Complete the calculate_guild_perms function. It takes as input four binary numbers representing the separate permissions of each member of the guild. It should return a single binary number that represents the combined permissions of all the members of the guild.
    perms = 0b0000
    for user in users :
        perms = perms | user
    return perms, bin(perms)

# 7 damage meter

def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")
    # not supposed to edit function. Supposed to fix test cases:
    # calculate_dps(8, 000, 000, 45) -> calculate_dps(8_000_000, 45)
    # calculate_dps(10, 000, 000, 49) -> calculate_dps(10_000_000, 49)

# 8 Converting Binary

def binary_string_to_int(num_servers, num_players, num_admins):
    # Complete the binary_string_to_int function. It takes three binary strings as input and returns each of them in the same order as integers. Each integer is the numerical value of the string when interpreted as binary.
    return int(num_servers,2), int(num_players,2), int(num_admins,2)


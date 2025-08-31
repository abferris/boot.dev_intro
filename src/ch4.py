# Chapter 4: Scope

# 1 global scope: they wanted a variable of player level above so it would apply. putting it in function.
def health_and_primary_stats(player_level):

    # Don't touch below this line
    def calculate_health(modifier):
        return player_level * modifier


    def calculate_primary_stats(armor_bonus, modifier):
        return armor_bonus + modifier + player_level


    print(f"Character has {calculate_health(10)} max health.")

    print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")



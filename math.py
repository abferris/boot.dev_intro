sword_damage = 10
start_health = 100
end_health = start_health - sword_damage

# Don't touch below this line
printable1 = f"Sam's health is: {start_health}"
printable2 = f"Sam takes {sword_damage} damage..."
printable3 = f"Sam's health is: {end_health}"

def printable():
    return f"{printable1}\n{printable2}\n{printable3}"

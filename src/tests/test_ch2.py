print("running ch2 tests")

import unittest
from io import StringIO
from contextlib import redirect_stdout
import src.ch2 as two

def capture_output(func, *args, **kwargs):
    buffer = StringIO()
    with redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue()

class TestPrintTwo(unittest.TestCase):
    
    def test_var(self):
        output = two.return_variable(100)
        expected_output = 100
        self.assertEqual(output, expected_output)
    
    def test_four_hit(self):
        output = capture_output( two.four_hits,100,15 )
        expected_output = "85\n70\n55\n40\n"
        self.assertEqual(output, expected_output)
    
    def test_armor_calc(self):
        output = two.armor_calc(100,1.25)
        expected_output = 125
        self.assertEqual(output, expected_output)

    def test_psn_damage(self):
        health = 100
        output = two.psn_damage(health)
        expected_output = 90
        self.assertEqual(output, expected_output)

    def test_ideal_weapon(self):
        output = two.ideal_weapon("sword")
        expected_output = "Perfect sword"
        self.assertEqual(output, expected_output)

    def test_define_types(self):
        player_health = 100
        player_class = "Wizard"
        alive = True
        targeted_enemy = None
        armor = 1.25
        dict1 = dict(health=player_health, job=player_class, active=alive, armored_health=player_health*armor)
        char = {
            "health" :  player_health,
            "job" :  player_class,
            "active" :  alive,
            "armored_health" :  player_health*armor
        }
        input_array = [player_health,player_class, alive, targeted_enemy, armor, dict1, char]
        output = list(map(two.define_types, input_array))    
        expected_output = ["int", "str", "bool", "NoneType", "float", "dict", "dict"]
    
        self.assertEqual(output, expected_output)

    def test_reset_enemy(self):
        output = two.reset_enemy()
        expected_output =  True
        self.assertEqual(output, expected_output)

    def test_health_message(self):
        output = two.health_message("Steve")
        expected_output = "Steve has a max health of 1200"
        self.assertEqual(output, expected_output)

    def test_quest_messages(self):
        output = capture_output(two.quest_messages)
        expected_output = "You there! Adventurer!\nThe local mine has been taken over by orcs!\nWe need your help taking it back. Bring back 8 of their axes as proof of your hard work.\n"
        self.assertEqual(output, expected_output)

    def test_avg_score(self):
        output = two.avg_score(1,2,5,6,1)
        expected_output = 3
        self.assertEqual(output,expected_output)
    
    def test_char_rep(self):
        output = capture_output(two.char_rep, "Steve", 5, "fighter", "fire", True)
        expected_output = "Character Report\n Steve is a level 5 fighter.\n They have fire magic resistance.\nTheir account is currently active: True\n=========================\nCharacter Report Complete\nData types:\nname: str, level: int, character_class: str\nmagic_resistance: str\naccount_active: bool"


if __name__ == "__main__":
    unittest.main()
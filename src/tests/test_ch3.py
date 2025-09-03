print('running ch3 tests')

import unittest
from io import StringIO
from contextlib import redirect_stdout
import src.ch3 as three

def capture_output(func, *args, **kwargs):
    buffer = StringIO()
    with redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue()

class TestPrintThree(unittest.TestCase):

    
    def test_attack_area(self):
        output = capture_output(three.attack_area, "spear", 2.0)
        expected_output = "spear length: 2.0 meters.\nspear attack area: 12.56 square meters.\n"
        self.assertEqual(output, expected_output)

    def test_triple_attack(self):
        output = capture_output(three.print_triple_attack,2,4,3)
        expected_output = "Attacking for 2 4 and 3 ...\n9 points of damage dealt!\n=====================================\n"
        self.assertEqual(output,expected_output)

    def test_char_report(self):
        output = capture_output(three.char_report,"Aragorn", "son of Arithorn", "ranger")
        expected_output = f"First name: Aragorn\nLast name: son of Arithorn\nJob: ranger\nTitle: Aragorn son of Arithorn the ranger\n=====================================\n"
        self.assertEqual(output,expected_output)
    
    def test_bootup_message(self):
        output = capture_output(three.bootup_message)
        expected_output = "Fantasy Quest is booting up...\nGame is running!\n"
        self.assertEqual(output,expected_output)

    def test_farenheight_to_celcius(self):    
        output = three.farenheight_to_celcius(100)
        expected_output = "100 degrees fahrenheit is 37.78 degrees celsius"
        self.assertEqual(output,expected_output)

    def test_hours_seconds_conversion(self):
        output = three.hours_seconds_conversion(25)
        expected_output = "25 hours is 90000 seconds"
        self.assertEqual(output,expected_output)

    def test_return_warrior(self):
        output = three.return_warrior("Aragorn son of Arithorn",600)
        expected_output = "Aragorn son of Arithorn the warrior has a power level of 601"
        self.assertEqual(output,expected_output)

    def test_test_damage(self):
        output = capture_output(three.test_damage,300,25)
        expected_output = "Running tests for health 300 and armor 25\n========================================\nHealth: 300, Armor: 25\nHealth after punch: 275\n----------------------------------------\nHealth: 300, Armor: 25\nHealth after slash: 225\n----------------------------------------\nHealth: 300, Armor: no armor!\nHealth after slash: 250\n----------------------------------------\nHealth: 300, Armor: no armor!\nHealth after punch: 200\n----------------------------------------\n"

    def test_curse_options(self):
        output = capture_output(three.curse_options,500)
        expected_output = "Weapon's base damage: 500.0\nCursing...\nWith lesser curse the damage is: 250.0 damage.\nWith greater curse the damage is: 125.0 damage.\n=====================================\n"
        self.assertEqual(output,expected_output)
        
    def test_enchant_attack(self):
        output = capture_output(three.enchant_attack,500,100,"axe")
        expected_output = "The target has 500 health.\naxe base damage: 100... Enchanting and attacking.\nThe target has been attacked with the enchanted axe.\nThe target has 390 health remaining.\n=====================================\n"
        self.assertEqual(output,expected_output)


if __name__ == "__main__":
    unittest.main()
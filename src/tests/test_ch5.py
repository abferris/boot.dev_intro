print('running ch5 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.tests.base_test import Tests
from src.ch5 import *



class Ch5Test(Tests):
    def test_total_xp(self):
        test_cases = [
            (1, 200, 300),
            (2, 50, 250),
            (0, 0, 0),
            (0, 200, 200),
            (176, 350, 17950),
            (250, 100, 25100),
        ]

        self.run_cases(total_xp,test_cases)   
    
    def test_take_magic_damage(self):
        run_cases = [
        (100, 5, 2, 20, 65),
        (200, 10, 1, 25, 185),
        (0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1),
        (100, 2, 3, 1, 99),
        (2500, 3, 2, 2, 2499),
        ]
        self.run_cases(take_magic_damage,run_cases)   

    def test_unlock_achievement(self):
        run_cases = [
        (100, 20, "Speedster", (120, "Achievement Unlocked: Speedster")),
        (200, 50, "Killer", (250, "Achievement Unlocked: Killer")),
        (100, 50, "Unstoppable", (150, "Achievement Unlocked: Unstoppable")),
        (400, 75, "Gnarly", (475, "Achievement Unlocked: Gnarly"))]
        self.run_cases(unlock_achievement,run_cases)   

    def test_create_stats_message(self):
        run_cases = [
        (1, 2, 3, "You have 1 strength, 2 wisdom, and 3 dexterity for a total of 6 stats."),
        (2, 4, 2, "You have 2 strength, 4 wisdom, and 2 dexterity for a total of 8 stats."),
        (10,50,100,"You have 10 strength, 50 wisdom, and 100 dexterity for a total of 160 stats."),
        (0, 0, 0, "You have 0 strength, 0 wisdom, and 0 dexterity for a total of 0 stats."),
        (1, 1, 1, "You have 1 strength, 1 wisdom, and 1 dexterity for a total of 3 stats.")]
        self.run_cases(create_stats_message,run_cases)   


if __name__ == "__main__":
    unittest.main()
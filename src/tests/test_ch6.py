print('running ch6 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.tests.base_test import Tests
from src.ch6 import *



class Ch6Test(Tests):
    def test_calculate_damage(self):
        run_cases = [
            (1, 2, 3, 4, 5, (15, 3.0)),
            (0, 0, 0, 0, 10, (10, 2.0)),
            (0, 0, 0, 0, 0, (0, 0.0)),
            (10, 20, 30, 40, 50, (150, 30.0)),
            (2, 2, 2, 2, 2, (10, 2.0)),
            (1, 1, 1, 1, 1, (5, 1.0))
        ]

        self.run_cases(calculate_damage,run_cases)   
    
    def test_update_player_score(self):
        run_cases = [
            (300, 300, 600),
            (600, 50, 650),
            (0, 0, 0),
            (1, 1, 2),
            (100, -50, 50),
        ]
        self.run_cases(update_player_score,run_cases)   

    def test_get_hurt(self):
        run_cases = [
            (840, 10, 830),
            (830, 3, 827),
            (0, 0, 0),
            (1, 1, 0),
            (100, 2, 98),
            (2500, 3, 2497),
            ]
        self.run_cases(get_hurt,run_cases)   

    def test_max_players_on_server(self):
        run_cases = [
        (1.024e18, 1.024e19, 1.024e20),
        ]
        self.run_cases(max_players_on_server,run_cases,False,0,3)   

    def test_perm_bits(self):
        run_cases = [
            (0b0110, False, True, True, False),
            (0b1111, True, True, True, True),
            (0b0000, False, False, False, False),
            (0b1001, True, False, False, True),
            (0b1000, True, False, False, False),
            (0b0100, False, True, False, False),
            (0b0010, False, False, True, False),
        ]
        self.run_cases(perm_bits,run_cases,False,1,4)   

    def test_calculate_guild_perms(self):
        run_cases = [
            (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),
            (0b0000, 0b0000, 0b0000, 0b1011, 0b1011),
            (0b1001, 0b0010, 0b1101, 0b1011, 0b1111),
        ]
        self.run_cases(calculate_guild_perms,run_cases,False,4,1)   

    def test_calculate_dps(self):
        run_cases = [
            (8_000_000, 45,177777.778),
            (10_000_000, 49,204081.633)
        ]
        self.run_cases(calculate_dps,run_cases,False,2,1)    

    def test_binary_string_to_int(self):
        run_cases = [
            ("1", "10", "1010", (1, 2, 10)),
            ("101", "11", "10100", (5, 3, 20)),
            ("111", "1011", "11010", (7, 11, 26)),
            ("0", "0", "0", (0, 0, 0)),
            ("1111", "1111", "1111", (15, 15, 15)),
            ("101010", "110011", "101010", (42, 51, 42)),
        ]
        self.run_cases(binary_string_to_int,run_cases)    

if __name__ == "__main__":
    unittest.main()
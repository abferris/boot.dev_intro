print('running ch7 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.tests.base_test import Tests
from src.ch7 import *

class Ch7Test(Tests):
    def test_player_1_wins(self):
        test_cases = [
            (5, 6, False),
            (5, 5, False),
            (7, 6, True),
            (10, 3, True),
            (2, 2, False),
            (0, 0, False),
            (10, 5, True),
            (5, 10, False),   
        ]

        self.run_cases(player_1_wins,test_cases)   
    
    def test_compare_heights(self):
        test_cases = [
            (5, 5, 7, 5, (True, True, False)),
            (6, 6, 5, 5, (False, True, False)),
            (4, 4, 4, 4, (True, True, True)),
            (2, 2, 2, 2, (True, True, True)),
            (8, 8, 8, 7, (False, True, True)),
            (5, 7, 9, 11, (False, False, False)),
            (11, 9, 7, 5, (False, False, False)),
        ]        
        self.run_cases(compare_heights,test_cases)

    def test_can_withstand_blow(self):
        test_cases = [(175, 250, False), (250, 175, True), (1, 1, True), (250, 250, True), (0, 0, True), (2, 3, False), (3, 2, True)]
        self.run_cases(can_withstand_blow,test_cases)
    
    def test_print_status(self):
        test_cases = [
            (0,"Dead\nstatus check complete\n"),
            (5,"Alive\nstatus check complete\n"),
            (-1,"Dead\nstatus check complete\n"),
            (3,"Alive\nstatus check complete\n")
        ]
        self.run_cases(print_status, test_cases)
    
    def test_check_swords_for_army(self):
        test_cases = [
            (500, 1000, "incorrect amount"),
            (800, 800, "correct amount"),
            (1500, 1000, "incorrect amount"),
            (200, 200, "correct amount"),
        ]
        self.run_cases(check_swords_for_army,test_cases)
    
    def test_player_status(self):
        test_cases = [    
            (0, "dead"),
            (4, "injured"),
            (6, "healthy"),
            (5, "injured"),
            (1, "injured"),
            (10, "healthy"),
            (-1, "dead"),
        ]
        self.run_cases(player_status,test_cases)
    
    def test_check_high_score_first(self):
        test_cases = [
            ("ash ketchum", "ash ketchum", "You are the highest scoring player!"),
            ("brock", "ash ketchum", "You are not the highest scoring player!"),
            ("misty", "brock", "You are not the highest scoring player!"),
            ("", "", "You are the highest scoring player!"),
            ("same", "same", "You are the highest scoring player!"),
        ]
        self.run_cases(check_high_score_first,test_cases)
    
    def test_check_high_score_second(self):
        test_cases = [
            ("ash ketchum", "ash ketchum", "brock", "high"),
            ("brock", "ash ketchum", "brock", "low"),
            ("misty", "brock", "ash ketchum", "neither"),
            ("red", "red", "blue", "high"),
            ("blue", "red", "blue", "low"),
            ("green", "red", "blue", "neither"),
        ]
        self.run_cases(check_high_score_second,test_cases)
    
    def test_does_attack_hit(self):
        test_cases = [
            (17, 18, False),
            (20, 25, True),
            (2, 2, True),
            (1, 0, False),
            (16, 13, True),
            (5, 5, True),
            (1, 1, False),
            (20, 20, True),
            (15, 10, True),
            (2, 3, False),
        ]
        self.run_cases(does_attack_hit,test_cases)
    
    def test_should_serve_customer(self):
        test_cases = [
            (22, False, 10, True),
            (41, False, 1, False),
            (14, False, 7, False),
            (21, False, 5, True),
            (107, False, 9, True),
            (23, True, 5, False),
            (21, False, 4, False),
            (57, False, 11, False),
            (20, False, 5, False),
        ]
        self.run_cases(should_serve_customer,test_cases)
    
    def test_mount_rental(self):
        test_cases = [    
            (3, 4, "no charges yet"),
            (5, 2, "overtime charged"),
            (2, 2, "overtime charged"),
            (0, 1, "no charges yet"),
            (1, 1, "overtime charged"),
            (100, 2, "overtime charged"),
            (2500, 3, "overtime charged"),
        ]
        self.run_cases(mount_rental,test_cases)
    
    def test_combat_evaluation(self):
        test_cases = [    (101, 100, True, False, False),
            (50, 100, False, True, False),
            (100, 100, False, False, True),
            (150, 70, True, False, False),
            (80, 150, False, True, False),
            (0, 0, False, False, True),
            (1, 1, False, False, True),
            (1000, 500, True, False, False),
            (500, 1000, False, True, False),
        ]
        self.run_cases(combat_evaluation,test_cases,False,2,3)

if __name__ == "__main__":
    unittest.main()
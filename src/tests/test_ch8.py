print('running ch8 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.tests.base_test import Tests
from src.ch8 import *

class Ch8Test(Tests):
    def test_loops(self):
        expected = "".join(f"{i}\n" for i in range(99))
        test_cases = [
           ( expected,)
        ]

        self.run_cases(print_numbers,test_cases,True,0,1)   

    def test_print_numbers_two(self):
        expected = "".join(f"{i}\n" for i in range(199))
        test_cases = [
            ( expected,)
        ]

        self.run_cases(print_numbers_two,test_cases,True)   
        
    def test_print_numbers_from_five_to(self):
        test_cases = [
            (16, "".join(f"{i}\n" for i in range(5,16))),
            (6, "".join(f"{i}\n" for i in range(5,6))),
            (11, "".join(f"{i}\n" for i in range(5,11))),
        ]

        self.run_cases(print_numbers_from_five_to,test_cases,True)   

    def test_count_down(self):
        test_cases = [
            (10,0, "".join(f"{i}\n" for i in range(10, 0, -1))),
            (20,10, "".join(f"{i}\n" for i in range(20, 10, -1))),
            (15,11, "".join(f"{i}\n" for i in range(15, 11, -1))),
        ]

        self.run_cases(count_down,test_cases,True)   

    def test_sum_of_numbers(self):
        test_cases = [
            (0, 5, 10), 
            (0, 10, 45), 
            (10, 20, 145),
            (1, 100, 4950),
            (5, 50, 1215),
            (20, 30, 245),
            (50, 60, 545),
            (100, 110, 1045),
        ]

        self.run_cases(sum_of_numbers,test_cases)   

    def test_sum_of_odd_numbers(self):
        test_cases = [
            (4, 4),
            (6, 9),
            (0, 0),
            (1, 0),
            (2, 1),
            (4, 4),
            (10, 25),
            (15, 49),
        ]

        self.run_cases(sum_of_odd_numbers,test_cases)   

    def test_regenerate(self):
        test_cases = [
            (0, 10, 20, 9), 
            (0, 10, 4, 1), 
            (8, 10, 20, 10),
            (0, 0, 0, 0),
            (9, 10, 3, 9),
            (100, 100, 200, 100),
            (2, 110, 50, 26),
            (100, 1010, 2000, 1010),
        ]

        self.run_cases(regenerate,test_cases)   

    def test_countdown_to_start(self):
        test_cases = [
            ("Counting down to match start:\n10...\n9...\n8...\n7...\n6...\n5...\n4...\n3...\n2...\n1... Fight!\n")
        ]

        self.run_cases(countdown_to_start,test_cases,True,0,1)   

    def test_calculate_experience_points(self):
        test_cases = [
            (2, 5),
            (3, 15),
            (4, 30),
            (1, 0),
            (5, 50),
            (7, 105),
            (10, 225),
            (15, 525),
            (20, 950),
        ]

        self.run_cases(calculate_experience_points,test_cases,False,1,1)   

    def test_meditate(self):
        test_cases = [
            (0, 10, 9, [9, 0]),
            (0, 12, 20, [12, 8]),
            (1, 100, 80, [81, 0]),
            (0, 0, 0, [0, 0]),
            (1000, 1000, 5, [1000, 5]),
            (0, 10, 5, [5, 0]),
            (5, 2000, 500, [505, 0]),
        ]

        self.run_cases(meditate,test_cases)   

if __name__ == "__main__":
    unittest.main()
print('running ch10 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.tests.base_test import Tests
from src.ch11 import *

class Ch11Test(Tests):
    def test_remove_duplicates(self):
        test_cases = [
            (
                [
                    "fireball",
                    "eldritch blast",
                    "fireball",
                    "eldritch blast",
                    "chill touch",
                    "eldritch blast",
                    "chill touch",
                    "chill touch",
                    "fireball",
                    "fireball",
                    "shocking grasp",
                    "fireball",
                    "fireball",
                ],
                ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
            ),
            (["fireball", "fireball", "fireball"], ["fireball"]),
            (
                ["fireball", "eldritch blast", "chill touch", "shocking grasp"],
                ["chill touch", "eldritch blast", "fireball", "shocking grasp"],
            ),
            (["chill touch", "chill touch", "chill touch"], ["chill touch"]),
            (["shocking grasp", "shocking grasp", "shocking grasp"], ["shocking grasp"]),
            ([], []),
            (["eldritch blast", "eldritch blast", "eldritch blast"], ["eldritch blast"]),
        ]
        self.run_cases(remove_duplicates,test_cases)
    
    def test_count_vowels(self):
        test_cases = [
            (
                "Did someone say Thunderfury, Blessed Blade of the Windseeker?",
                (19, {"u", "o", "i", "e", "a"}),
            ),
            ("LF9M UBRS NEED ALL!!!!", (4, {"U", "E", "A"})),
            ("Leatherworker LFW Have all end game recipes!", (14, {"e", "i", "o", "a"})),
            ("", (0, set())),
            (
                "Can anyone spare 1g so I can train my new spells?",
                (13, {"o", "I", "i", "e", "a"}),
            ),
            ("no", (1, {"o"})),
            ("mages need a nerf", (6, {"e", "a"})),
            ("wtb port to Roshar", (4, {"o", "a"})),
        ]
        self.run_cases(count_vowels,test_cases)
    
    def test_find_missing_ids(self):
        test_cases = [
            ([1, 1, 1, 2, 2, 2, 3], [1, 2], {3}),
            ([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 5, 6, 7, 8], {9, 10}),
            ([], [], set()),
            ([1, 1, 1], [], {1}),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], set()),
            ([1, 1, 2, 2, 3, 3], [1, 2, 3], set()),
            ([1, 2, 3, 4, 5], [1, 2, 3], {4, 5}),
            ([1, 2, 3, 4, 5], [1, 3, 5], {2, 4}),
        ]
        self.run_cases(find_missing_ids,test_cases)
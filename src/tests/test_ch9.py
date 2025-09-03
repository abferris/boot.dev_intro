print('running ch9 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.tests.base_test import Tests
from src.ch9 import *

class Ch9Test(Tests):
    def test_get_inventory(self):
        test_cases = [
            ( ["Healing Potion", "Leather Scraps", "Iron Helmet", "Short Sword"],)
        ]

        self.run_cases(get_inventory,test_cases)   

    def test_get_leather_scraps(self):
        test_cases = [
            ("Leather Scraps",)
        ]
        self.run_cases(get_leather_scraps,test_cases)   
    
    def test_get_last_index(self):
        test_cases = [
            (["Potion"], 0),
            (["Potion", "Iron Breastplate"], 1),
            (["Potion", "Iron Breastplate", "Bread", "Longsword"], 3),
            ([], -1),
            (["Single item"], 0),
            (["Shield", "Sword", "Bow", "Arrows", "Health Potion"], 4),
            (["Shield", "Sword", "Bow"], 2),
            (["Shield", "Sword"], 1),
        ]
        self.run_cases(get_last_index,test_cases)

    def test_smelt_ore(self):
        test_cases = [
            (
                ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
                ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
            ),
            ([None, None, None, None], [None, None, None, None]),
            (["Potion", "Iron Ore", None, None], ["Potion", "Iron Bar", None, None]),
            (
                [None, "Iron Ore", None, "Leather Armor"],
                [None, "Iron Bar", None, "Leather Armor"],
            ),
        ]
        self.run_cases(smelt_ore,test_cases)

    def test_generate_user_list(self):
        test_cases = [
            (5, list(range(5))),
            (10, list(range(10))),
            (0, []),
            (1, [0]),
            (100, list(range(100))),
            (25, list(range(25))),
            (50, list(range(50))),
        ]
        self.run_cases(generate_user_list,test_cases)

    def test_clear_inventory(self):
        inventory = [
            "Healing Potion",
            "Iron Bar",
            "Kite Shield",
            "Shortsword",
            "Leather Scraps",
            "Tattered Cloth",
        ]
        expected_output = """inventory: ['Healing Potion', 'Iron Bar', 'Kite Shield', 'Shortsword', 'Leather Scraps', 'Tattered Cloth']
Selling: Tattered Cloth
inventory: ['Healing Potion', 'Iron Bar', 'Kite Shield', 'Shortsword', 'Leather Scraps']
Selling: Leather Scraps
inventory: ['Healing Potion', 'Iron Bar', 'Kite Shield', 'Shortsword']
Selling: Shortsword
inventory: ['Healing Potion', 'Iron Bar', 'Kite Shield']
Selling: Kite Shield
inventory: ['Healing Potion', 'Iron Bar']
Selling: Iron Bar
inventory: ['Healing Potion']
Selling: Healing Potion
inventory: []
"""
        test_cases = [
            ( inventory,expected_output)
        ]
        self.run_cases(clear_inventory,test_cases,True)

    def test_get_item_counts(self):
        test_cases = [
            (["Bread", "Potion", "Shortsword", "Bread"], (1, 2, 1)),
            (["Potion", "Potion", "Shortsword", "Buckler", "Iron Mace"], (2, 0, 1)),
            ([], (0, 0, 0)),
            (["Potion", "Leather Scraps", "Bread", "Iron Ore", "Light Leather", "Bread", "Shortsword", "Longsword", "Ironwood Branch", "Shortsword", "Shortsword",],(1, 2, 3),),
            (["Bread", "Bread", "Bread", "Bread"], (0, 4, 0)),
            (["Shortsword", "Shortsword", "Shortsword", "Shortsword"], (0, 0, 4)),
            (["Potion"], (1, 0, 0)),
            (["Potion", "Bread", "Shortsword"], (1, 1, 1)),
        ]
        self.run_cases(get_item_counts,test_cases)

    def test_contains_leather_scraps(self):
        test_cases = [
            (["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"], True),
            (["Potion", "Shortsword", "Buckler", "Iron Mace"], False),
            ([], False),
            (["Leather Scraps"], True),
            (["Potion", "Leather Scraps", "Leather Scraps"], True),
            (["Potion", "Healing Potion"], False),
            (["Leather scraps"], False),
            (["Leather", "Scraps"], False),
        ]
        self.run_cases(contains_leather_scraps,test_cases)

    def test_check_character_levels(self):
        old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
        new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]
        test_cases = [
            (old_character_levels, new_character_levels, f"Player 2 Leveled up\nPlayer 3 Leveled up\nPlayer 7 Leveled up\n" )
        ]
        self.run_cases(check_character_levels,test_cases,True)

    def test_find_max(self):
        test_cases = [
            ([1, 2, 3, 4, 5], 5), 
            ([1, 2, 300, 4, 5], 300),
            ([1, 20, 3, 4, 5], 20),
            ([-1, 2, 3, 4, 5], 5),
            ([1, 2, 3, 21, 18], 21),
            ([], float("-inf")),
            ([-1, -2, -3, -4, -5], -1),
        ]
        self.run_cases(find_max,test_cases)

    def test_get_odd_numbers(self):
        test_cases = [
            (10, [1, 3, 5, 7, 9]), 
            (20, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),
            (0, []),
            (1, []),
            (2, [1]),
            (300, [i for i in range(1, 300, 2)]),
        ]
        self.run_cases(get_odd_numbers,test_cases,False)

    def test_get_champion_slices(self):
        test_cases = [
            (
                ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad", "Gilforn"],
                (
                    ["Gandolfo", "Thraine", "Norwad", "Gilforn"],
                    ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad"],
                    ["Thrundar", "Gandolfo", "Norwad"],
                ),
            ),
            (
                ["Frank", "Dennis", "Sweet Dee", "Mac", "Charlie"],
                (
                    ["Sweet Dee", "Mac", "Charlie"],
                    ["Frank", "Dennis", "Sweet Dee", "Mac"],
                    ["Frank", "Sweet Dee", "Charlie"],
                ),
            ),
            (([]), ([], [], [])),
            (
                (["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon", "Tony"]),
                (
                    ["Spencer", "Bill", "Matthew", "Brandon", "Tony"],
                    ["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon"],
                    ["John", "Spencer", "Matthew", "Tony"],
                ),
            ),
        ]
        self.run_cases(get_champion_slices,test_cases)

    def test_concatenate_favorites(self):
        test_cases = [
            (["sword", "dagger"], ["bracers", "helmet"], ["feather", "iron bars"], ["sword", "dagger", "bracers", "helmet", "feather", "iron bars"]),
            (["lance"], ["shield"], ["potions"], (["lance", "shield", "potions"]),),
            (["bow", "staff"],["breastplate"],["scrolls", "bedroll"],(["bow", "staff", "breastplate", "scrolls", "bedroll"]),),
            ([], [], [], ([])),
        ]
        self.run_cases(concatenate_favorites,test_cases)

    def test_is_top_weapon(self):
        test_cases = [
            ("sword of justice", True),
            ("bronze mace", False),
            ("sword of slashing", True),
            ("", False),
            ("great axe", True),
            ("silver bow", True),
            ("golden spear", False),
            ("spiked knuckles", True),
            ("spellbook", True),
        ]
        self.run_cases(is_top_weapon,test_cases)

    def test_trim_strongholds(self):
        test_cases = [
            (
                [
                    "Rivendale",
                    "The Morgoth Mountains",
                    "The Lonely Island",
                    "Mordia",
                    "Mordane",
                    "Gondolin",
                ],
                [
                    "The Morgoth Mountains",
                    "The Lonely Island",
                    "Mordia",
                ],
            ),
            (
                [
                    "Pogsmeade",
                    "Dogwarts",
                    "The Leaky Pot",
                    "The Screaming Hut",
                ],
                [
                    "Dogwarts",
                ],
            ),
            (
                [
                    "Midgard",
                    "Cosmo Canyon",
                    "Nibelheim",
                    "Costa del Sol",
                    "Pallet Town",
                    "Viridian City",
                    "Salamandastron",
                    "Redwall Abbey",
                    "Fisherman's Horizon",
                    "Waterdeep",
                    "Elturel",
                    "Candlekeep",
                    "Chult",
                    "Eorzea",
                    "Ratchet",
                    "Orgrimmar",
                    "Stormwind",
                    "Shattrath",
                    "Dalaran",
                ],
                [
                    "Cosmo Canyon",
                    "Nibelheim",
                    "Costa del Sol",
                    "Pallet Town",
                    "Viridian City",
                    "Salamandastron",
                    "Redwall Abbey",
                    "Fisherman's Horizon",
                    "Waterdeep",
                    "Elturel",
                    "Candlekeep",
                    "Chult",
                    "Eorzea",
                    "Ratchet",
                    "Orgrimmar",
                    "Stormwind",
                ],
            ),
        ]
        self.run_cases(trim_strongholds,test_cases)

    def test_get_heroes(self):
        inputs = ["Glorfindel",2093,True,"Gandalf",1054,False,"Gimli",389,False,"Aragorn",87,False,]
        test_cases = [
            (inputs, [("Glorfindel",2093,True,),("Gandalf",1054,False,),("Gimli",389,False,),("Aragorn",87,False,),]),
        ]
        self.run_cases(get_heroes,test_cases)

    def test_get_first_item(self):
        test_cases = [
            ([1, 2], 1),
            (["Healing Potion"], "Healing Potion"),
            ([], "ERROR"),
            (["Iron Ore", "Iron Bar", "Scimitar"], "Iron Ore"),
            (["Apple", "Banana", "Cherry"], "Apple"),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]),
            ([False, True, False], False),
        ]
        self.run_cases(get_first_item,test_cases)

    def test_reverse_list(self):
        test_cases = [
            (["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"],["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"],),
            ([1, 2, 300, 4, 5], [5, 4, 300, 2, 1]),
            ([], []),
            (["a"], ["a"]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
            (
                ["apple", "banana", "cherry", "date", "elderberry"],
                ["elderberry", "date", "cherry", "banana", "apple"],
            ),
            (["hello", "world"], ["world", "hello"]),
        ]
        self.run_cases(reverse_list,test_cases)

    def test_filter_messages(self):
        test_cases = [
            (["darn it", "this dang thing won't work", "lets fight one on one"],
            ["darn it", "this thing won't work", "lets fight one on one"],
            [0, 1, 0],),
            ([
                "well dang it",
                "dang the whole dang thing",
                "kill that knight, dang it",
                "get him!",
                "donkey kong",
                "oh come on, get them",
                "run away from the dang baddies",
            ],
            [
                "well it",
                "the whole thing",
                "kill that knight, it",
                "get him!",
                "donkey kong",
                "oh come on, get them",
                "run away from the baddies",
            ],
            [1, 2, 1, 0, 0, 0, 1],)
        ]
        self.run_cases(filter_messages,test_cases,False,1,2)

    def test_split_players_into_teams(self):
        test_cases = [
            (["Harry","Hermione","Ron","Ginny","Fred","Neville","Draco","Luna","Cho","Gregory","Lee","Michael","Lavender","Frank","Anthony","Allan"],(["Harry", "Ron", "Fred", "Draco", "Cho", "Lee", "Lavender", "Anthony"],["Hermione","Ginny","Neville","Luna","Gregory","Michael","Frank","Allan",],),),
            (["Mike", "Walter", "Skyler", "Tuco"], (["Mike", "Skyler"], ["Walter", "Tuco"])), 
            (["Alice", "Bob", "Charlie", "David"], (["Alice", "Charlie"], ["Bob", "David"])),
            ([], ([], [])),
        ]
        self.run_cases(split_players_into_teams,test_cases)

    def test_check_ingredient_match(self):
        test_cases = [
            (
                [
                    "Mandrake Root",
                    "Griffin Feather",
                    "Elf Dust",
                    "Goblin Ear",
                ],
                [
                    "Elf Dust",
                    "Goblin Ear",
                ],
                (50.0, ["Mandrake Root", "Griffin Feather"]),
            ),
            (
                [
                    "Dragon Scale",
                    "Unicorn Hair",
                    "Phoenix Feather",
                    "Troll Tusk",
                    "Mandrake Root",
                    "Griffin Feather",
                    "Elf Dust",
                    "Goblin Ear",
                ],
                [
                    "Dragon Scale",
                    "Phoenix Feather",
                    "Mandrake Root",
                    "Griffin Feather",
                    "Elf Dust",
                    "Goblin Ear",
                ],
                (75.0, ["Unicorn Hair", "Troll Tusk"]),
            ),
            (
                [
                    "Dragon Scale",
                    "Phoenix Feather",
                    "Troll Tusk",
                    "Mandrake Root",
                    "Griffin Feather",
                    "Elf Dust",
                    "Goblin Ear",
                    "Unicorn Hair",
                ],
                [
                    "Goblin Ear",
                    "Elf Dust",
                    "Griffin Feather",
                    "Mermaid Tear",
                    "Goblin Ear",
                    "Phoenix Feather",
                    "Troll Tusk",
                    "Unicorn Hair",
                ],
                (
                    75.0,
                    [
                        "Dragon Scale",
                        "Mandrake Root",
                    ],
                ),
            ),
            (
                [
                    "Orc Tears",
                    "Ogre Ear",
                    "Goblin Giggles",
                    "Witch Broom",
                    "Giant Toenail Clipping",
                    "Centipede Foot",
                    "Dog Hair",
                    "Bald Eagle Dandruff",
                ],
                [
                    "Unicorn Hair",
                    "Dragon Scale",
                    "Phoenix Feather",
                    "Troll Tusk",
                    "Griffin Feather",
                    "Mandrake Root",
                    "Goblin Ear",
                    "Bald Eagle Dandruff",
                ],
                (
                    12.5,
                    [
                        "Orc Tears",
                        "Ogre Ear",
                        "Goblin Giggles",
                        "Witch Broom",
                        "Giant Toenail Clipping",
                        "Centipede Foot",
                        "Dog Hair",
                    ],
                ),
            ),
        ]
        self.run_cases(check_ingredient_match,test_cases)

    # def test_print_numbers_two(self):
    #     test_cases = [
    #         ( expected,)
    #     ]
    #     self.run_cases(print_numbers_two,test_cases)

    # def test_print_numbers_two(self):
    #     test_cases = [
    #         ( expected,)
    #     ]
    #     self.run_cases(print_numbers_two,test_cases
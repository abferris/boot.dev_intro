print('running ch10 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.tests.base_test import Tests
from src.ch10 import *

class Ch10Test(Tests):
    def test_get_character_record(self):
        test_cases = [
            (
                "bloodwarrior123",
                "server1",
                5,
                1,
                {
                    "name": "bloodwarrior123",
                    "server": "server1",
                    "level": 5,
                    "rank": 1,
                    "id": "bloodwarrior123#server1",
                },
            ),
            (
                "fronzenboi",
                "server2",
                2,
                1,
                {
                    "name": "fronzenboi",
                    "server": "server2",
                    "level": 2,
                    "rank": 1,
                    "id": "fronzenboi#server2",
                },
            ),
            (
                "slasher69",
                "server3",
                2,
                5,
                {
                    "name": "slasher69",
                    "server": "server3",
                    "level": 2,
                    "rank": 5,
                    "id": "slasher69#server3",
                },
            ),
            (
                "icequeen",
                "server4",
                3,
                2,
                {
                    "name": "icequeen",
                    "server": "server4",
                    "level": 3,
                    "rank": 2,
                    "id": "icequeen#server4",
                },
            ),
            (
                "shadowmaster",
                "server5",
                4,
                3,
                {
                    "name": "shadowmaster",
                    "server": "server5",
                    "level": 4,
                    "rank": 3,
                    "id": "shadowmaster#server5",
                },
            ),
            (
                "silentslasher",
                "server6",
                5,
                4,
                {
                    "name": "silentslasher",
                    "server": "server6",
                    "level": 5,
                    "rank": 4,
                    "id": "silentslasher#server6",
                },
            ),
            (
                "hypershadow",
                "server7",
                3,
                5,
                {
                    "name": "hypershadow",
                    "server": "server7",
                    "level": 3,
                    "rank": 5,
                    "id": "hypershadow#server7",
                },
            ),
        ]

        self.run_cases(get_character_record,test_cases) 

    def test_get_character_record_re(self):
        test_cases = [
            (
                "bloodwarrior123",
                "server1",
                5,
                1,
                {
                    "name": "bloodwarrior123",
                    "server": "server1",
                    "level": 5,
                    "rank": 1,
                    "id": "bloodwarrior123#server1",
                },
            ),
            (
                "fronzenboi",
                "server2",
                2,
                1,
                {
                    "name": "fronzenboi",
                    "server": "server2",
                    "level": 2,
                    "rank": 1,
                    "id": "fronzenboi#server2",
                },
            ),
            (
                "slasher69",
                "server3",
                2,
                5,
                {
                    "name": "slasher69",
                    "server": "server3",
                    "level": 2,
                    "rank": 5,
                    "id": "slasher69#server3",
                },
            ),
            (
                "kingofgames",
                "server4",
                3,
                2,
                {
                    "name": "kingofgames",
                    "server": "server4",
                    "level": 3,
                    "rank": 2,
                    "id": "kingofgames#server4",
                },
            ),
            (
                "godofwar",
                "server5",
                1,
                5,
                {
                    "name": "godofwar",
                    "server": "server5",
                    "level": 1,
                    "rank": 5,
                    "id": "godofwar#server5",
                },
            ),
            (
                "pythonista",
                "server6",
                4,
                3,
                {
                    "name": "pythonista",
                    "server": "server6",
                    "level": 4,
                    "rank": 3,
                    "id": "pythonista#server6",
                },
            ),
            (
                "codemaster",
                "server7",
                3,
                1,
                {
                    "name": "codemaster",
                    "server": "server7",
                    "level": 3,
                    "rank": 1,
                    "id": "codemaster#server7",
                },
            ),
        ]

        self.run_cases(get_character_record_re,test_cases)  

    def test_count_enemies(self):
        test_cases = [
            (["jackal", "kobold", "soldier"], {"jackal": 1, "kobold": 1, "soldier": 1}),
            (["jackal", "kobold", "jackal"], {"jackal": 2, "kobold": 1}),
            ([], {}),
            (["jackal"], {"jackal": 1}),
            (
                [
                    "jackal",
                    "kobold",
                    "jackal",
                    "kobold",
                    "soldier",
                    "kobold",
                    "soldier",
                    "soldier",
                    "jackal",
                    "jackal",
                    "gremlin",
                    "jackal",
                    "jackal",
                ],
                {"jackal": 6, "kobold": 3, "soldier": 3, "gremlin": 1},
            ),
            (["jackal", "kobold", "gremlin"], {"jackal": 1, "kobold": 1, "gremlin": 1}),
            (["jackal", "jackal", "jackal"], {"jackal": 3}),
            (["gremlin", "gremlin", "gremlin"], {"gremlin": 3}),
        ]

        self.run_cases(count_enemies,test_cases)  

    def test_get_most_common_enemy(self):
        test_cases = [
            ({"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5}, "soldier"),
            ({"jackal": 1, "kobold": 3, "soldier": 2, "gremlin": 5}, "gremlin"),
            ({"jackal": 2, "gremlin": 7}, "gremlin"),
            ({"jackal": 3}, "jackal"),
            ({}, None),
            ({"kobold": 5, "soldier": 5, "gremlin": 5, "dragon": 5}, "kobold"),
            ({"jackal": 5, "kobold": 3, "soldier": 10, "gremlin": 5, "dragon": 20}, "dragon"),
            ({"jackal": 5, "kobold": 3, "soldier": 2, "gremlin": 10, "dragon": 1}, "gremlin"),
        ]

        self.run_cases(get_most_common_enemy,test_cases)  

    def test_get_quest_status(self):
        test_cases = [
            (
                {
                    "entity": {
                        "character": {
                            "name": "Sir Galahad",
                            "quests": {
                                "bridge_run": {
                                    "status": "In Progress",
                                },
                                "talk_to_syl": {
                                    "status": "Completed",
                                },
                            },
                        }
                    }
                },
                "In Progress",
            ),
            (
                {
                    "entity": {
                        "character": {
                            "name": "Lady Gwen",
                            "quests": {
                                "bridge_run": {
                                    "status": "Completed",
                                },
                                "talk_to_syl": {
                                    "status": "In Progress",
                                },
                            },
                        }
                    }
                },
                "Completed",
            ),
            (
                {
                    "entity": {
                        "character": {
                            "name": "Archer Finn",
                            "quests": {
                                "bridge_run": {
                                    "status": "Not Started",
                                },
                                "talk_to_syl": {
                                    "status": "Completed",
                                },
                            },
                        }
                    }
                },
                "Not Started",
            ),
            (
                {
                    "entity": {
                        "character": {
                            "name": "Mage Elara",
                            "quests": {
                                "bridge_run": {
                                    "status": "Failed",
                                },
                                "talk_to_syl": {
                                    "status": "Completed",
                                },
                            },
                        }
                    }
                },
                "Failed",
            ),
            (
                {
                    "entity": {
                        "character": {
                            "name": "Rogue Talon",
                            "quests": {
                                "bridge_run": {
                                    "status": "Completed",
                                },
                                "talk_to_syl": {
                                    "status": "Not Started",
                                },
                            },
                        }
                    }
                },
                "Completed",
            ),
        ]

        self.run_cases(get_quest_status,test_cases)  


    def test_merge(self):
        test_cases = [
            (
                {"Goku": 8000, "Vegeta": 7500},
                {"Piccolo": 3500, "Gohan": 2800},
                {
                    "Goku": 8000,
                    "Vegeta": 7500,
                    "Piccolo": 3500,
                    "Gohan": 2800,
                },
            ),
            (
                {"Frieza": 120000, "Cell": 900000},
                {"Majin_Buu": 1100000, "Broly": 10000},
                {
                    "Frieza": 120000,
                    "Cell": 900000,
                    "Majin_Buu": 1100000,
                    "Broly": 10000,
                },
            ),
            (
                {
                    "Android_17": 30000,
                    "Android_18": 30000,
                    "Future_Trunks": 9000,
                    "Kid_Trunks": 7000,
                },
                {
                    "Android_17": 40000,
                    "Dr_Gero": 10000,
                    "Goten": 6500,
                    "Future_Gohan": 8000,
                },
                {
                    "Android_17": 40000,
                    "Android_18": 30000,
                    "Dr_Gero": 10000,
                    "Future_Trunks": 9000,
                    "Kid_Trunks": 7000,
                    "Goten": 6500,
                    "Future_Gohan": 8000,
                },
            ),
        ]

        self.run_cases(merge,test_cases)

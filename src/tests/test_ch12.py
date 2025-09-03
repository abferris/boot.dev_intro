print('running 12 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.tests.base_test import Tests
from src.ch12 import *

class Ch12Test(Tests):
    def test_get_player_record_1(self):
        test_cases = [
            (1,{"name": "Slayer", "level": 128}),
            (2,{"name": "Dorgoth", "level": 300}),
            (3,{"name": "Saruman", "level": 4000})
        ]
        invalid_cases = [
            (4,)
        ]
        self.assert_raises(get_player_record_1, Exception, invalid_cases, expected_message="player id not found")

        self.run_cases(get_player_record_1,test_cases)
        
    def test_get_player_record_2(self):
        test_cases = [
            (1, {"name": "Slayer", "level": 128}),
            (3, {"name": "Saruman", "level": 4000}),
            (2, {"name": "Dorgoth", "level": 300}),

        ]

        invalid_cases = [
            (4,),
            (5,),
            (0,),
        ]
        error_message = 'Nonexistent player ID!'

        self.assert_raises(get_player_record_2, Exception, invalid_cases, expected_message= error_message)
        self.run_cases(get_player_record_2,test_cases)

    def test_process_player_record(self):
        test_cases = [
            (0, {"name": "Slayer", "level": 128}),
            (1, {"name": "Dorgoth", "level": 300}),
            (2, {"name": "Saruman", "level": 4000}),
        ]

        invalid_cases_1 = [
            (-1,),
            (-5,),
        ]
        invalid_cases_2 = [
            (3,),
            (10,),
        ]
        error_message_1 = 'negative ids not allowed'
        error_message_2 = 'index is too high'

        self.assert_raises(process_player_record, Exception, invalid_cases_1, expected_message= error_message_1)
        self.assert_raises(process_player_record, Exception, invalid_cases_2, expected_message= error_message_2)
        self.run_cases(process_player_record,test_cases)

    def test_purchase_item(self):
        test_cases = [
            (10.00, 20.00, 10.00),
            (15.10, 15.10, 0.00),
            (7.50, 7.50, 0.00),
            (0.00, 0.00, 0.00),
        ]
        error_inputs = [
            (1430.00, 69.00),(30.00, 20.00),(100.00, 99.99)
        ]
        error_output = "not enough gold"
    
        self.assert_raises(purchase_item, Exception, error_inputs, expected_message=error_output)

        self.run_cases(purchase_item,test_cases)

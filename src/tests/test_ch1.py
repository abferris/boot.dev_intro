import unittest
from io import StringIO
from contextlib import redirect_stdout

from src import ch1 as one

def capture_output(func, *args, **kwargs):
    buffer = StringIO()
    with redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue()

class TestPrintOne(unittest.TestCase):
    
    def test_title(self):
        output = capture_output(one.title)
        expected_output = 'Welcome to Fantasy Quest!\n'
        self.assertEqual(output, expected_output)
    
    def test_bugfix(self):
        output = capture_output(one.bugfix)
        expected_output = "Sam's health is: 100\nSam takes 10 damage...\nSam's health is: 90\n"
        self.assertEqual(output, expected_output)
    
    def test_console(self):
        output = capture_output(one.the_console)
        expected_output = "Please move forward\n"
        self.assertEqual(output, expected_output)

    def test_addition_print(self):
        output = capture_output(one.addition_print)
        expected_output = '325\n'
        self.assertEqual(output, expected_output)

    def test_multiple_print(self):
        output = capture_output(one.mutiple_print)
        expected_output = """Jax: B-Kaw!
Hero: ...
Jax: Where are you off to this morning? Bkaw...
Hero: Where did an owl learn to speak??
"""
        # testing how triple quotes work
        self.assertEqual(output, expected_output)

    def test_syntax_erorrs(self):
        output = capture_output(one.syntax_errors)
        # testing how single quotes work        
        expected_output = 'Welcome to Fantasy Quest!\n'
        self.assertEqual(output, expected_output)

    def test_server_message(self):
        output = capture_output(one.server_message)
        expected_output =  'Starting up game server...\nlocal game server is listening on port 8080\n'
        self.assertEqual(output, expected_output)

    def test_basic_math(self):
        output = capture_output(one.basic_math)
        expected_output = '247.5\n'
        self.assertEqual(output, expected_output)

    def test_inkeeper_dialouge(self):
        output = capture_output(one.innkeeper_dialouge)
        expected_output = "The Innkeeper: Ah! Great choices...\nThe Innkeeper: Is there anything else I can help you with?\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
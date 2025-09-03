print('running ch4 tests')
import unittest
from io import StringIO
from contextlib import redirect_stdout
import src.ch4 as four

def capture_output(func, *args, **kwargs):
    buffer = StringIO()
    with redirect_stdout(buffer):
        func(*args, **kwargs)
    return buffer.getvalue()


class TestPrintThree(unittest.TestCase):
    def test_health_and_primary_stats(self):
        output = capture_output(four.health_and_primary_stats,8)
        expected_output = "Character has 80 max health.\nCharacter has 19 primary stats.\n"
        self.assertEqual(output,expected_output)


if __name__ == "__main__":
    unittest.main()
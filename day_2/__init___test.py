import unittest

from day_2 import process


class TestDay2(unittest.TestCase):
    def test_when_two_passwords_are_valid(self):
        input = [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc'
        ]

        self.assertEqual(2, process(data=input))

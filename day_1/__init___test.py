import unittest

import day_1


class TestDay1(unittest.TestCase):
    def test_when_using_two_entries(self):
        input = [
            1721,
            979,
            366,
            299,
            675,
            1456
        ]

        expected = 1721 * 299

        self.assertEqual(day_1.process(data=input, entry_count=2), expected)

    def test_when_using_three_entries(self):
        input = [
            1721,
            979,
            366,
            299,
            675,
            1456
        ]
        expected = 979 * 366 * 675
        self.assertEqual(day_1.process(data=input, entry_count=3), expected)

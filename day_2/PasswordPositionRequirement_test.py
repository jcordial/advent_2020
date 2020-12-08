import unittest

from day_2.PasswordPositionalRequirement import PasswordPositionalRequirement


class TestPasswordPositionalRequirement(unittest.TestCase):
    def test_when_password_is_valid(self):
        input = '1-3 a: abcde'
        validator = PasswordPositionalRequirement('a', 1, 3)
        self.assertTrue(validator.validate('abcde'))

    def test_when_password_is_invalid(self):
        # 1-3 b: cdefg
        validator = PasswordPositionalRequirement('b', 1, 3)
        self.assertFalse(validator.validate('cdefg'))

        validator = PasswordPositionalRequirement('c', 2, 9)
        self.assertFalse(validator.validate('ccccccccc'))

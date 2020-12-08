import unittest

from day_2 import PasswordValidator


class TestPasswordValidator(unittest.TestCase):
    def test_when_a_password_is_valid(self):
        input = '1-3 a: abcde'
        validator = PasswordValidator.from_string(input)
        self.assertTrue(validator.is_valid)

        input = '2-9 c: ccccccccc'
        validator = PasswordValidator.from_string(input)
        self.assertTrue(validator.is_valid)

    def test_when_a_password_is_invalid(self):
        input = '1-3 b: cdefg'
        validator = PasswordValidator.from_string(input)
        self.assertFalse(validator.is_valid)

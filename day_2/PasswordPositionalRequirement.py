from day_2.PasswordRequirement import PasswordRequirement


def test_position(password, position, test_string):
    return len(password) >= position and password[position - 1] == test_string


class PasswordPositionalRequirement(PasswordRequirement):
    def validate(self, password: str):
        low_valid = test_position(
            password, self.lower_number, self.test_string
        )
        high_valid = test_position(
            password, self.higher_number, self.test_string
        )
        return (low_valid or high_valid) and low_valid != high_valid

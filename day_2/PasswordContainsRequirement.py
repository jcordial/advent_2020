from day_2.PasswordRequirement import PasswordRequirement


class PasswordContainsRequirement(PasswordRequirement):
    def validate(self, password: str):
        occurrences = password.count(self.test_string)
        return self.higher_number >= occurrences >= self.lower_number

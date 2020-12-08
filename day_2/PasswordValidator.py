import typing

from day_2.PasswordContainsRequirement import PasswordContainsRequirement
from day_2.PasswordRequirement import PasswordRequirement


class PasswordValidator():
    requirements: typing.List[PasswordContainsRequirement]
    value: str

    def __init__(self, value: str = '', requirements: typing.List[PasswordContainsRequirement] = []) -> None:
        super().__init__()
        self.requirements = requirements
        self.value = value

    @property
    def is_valid(self):
        for requirement in self.requirements:
            if requirement.validate(self.value):
                continue
            return False
        return True

    @classmethod
    def from_string(
            cls,
            line: str,
            requirement_classes: typing.List[typing.Type[PasswordRequirement]]
    ) -> 'day_2.PasswordValidator.PasswordValidator':
        [minmax, required_character, password] = map(lambda s: s.strip(), line.split(' '))
        [lower_number, higher_number] = map(int, minmax.split('-'))
        required = required_character[0:-1]

        requirements = [requirement_class(required, lower_number, higher_number) for requirement_class in
                        requirement_classes]

        return PasswordValidator(password, requirements=requirements)

import typing
from functools import reduce

from day_2.PasswordContainsRequirement import PasswordContainsRequirement
from day_2.PasswordRequirement import PasswordRequirement
from day_2.PasswordValidator import PasswordValidator


def process(
        data: typing.Iterable[str],
        requirement_classes: typing.List[typing.Type[PasswordRequirement]] = [PasswordContainsRequirement]
):
    accum = 0
    for line in data:
        validator = PasswordValidator.from_string(line, requirement_classes)
        if validator.is_valid:
            accum += 1
    return accum

import typing
from functools import reduce
from itertools import combinations, permutations, product, tee


def accum(accum: int, value: int) -> int:
    return accum * value


def process(data: typing.Iterable[int], entry_count: int = 2) -> int:
    entries = combinations(data, entry_count)
    for combo in entries:
        sum_values, accum_values = tee(combo)
        if sum(sum_values) == 2020:
            return reduce(accum, accum_values)

    return 0

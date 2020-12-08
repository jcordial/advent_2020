import unittest
from itertools import tee
from math import prod

from day_3 import process, process_multiple


class TestDay3(unittest.TestCase):
    def test_should_collide_with_seven_trees(self):
        input = iter([
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#',
        ])
        self.assertEqual(process(data=input, acceleration=(3, 1)), 7)

    def test_when_multiple_accelerations_are_given(self):
        input = iter([
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#',
        ])
        results = list(process_multiple(
            data=input,
            accelerations=[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        ))
        self.assertEqual(prod(results), 336)
        expected = [2, 7, 3, 4, 2]
        self.assertCountEqual(results, expected)

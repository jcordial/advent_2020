from functools import reduce
from math import prod

import click
import day_1
import day_2
import day_3
from day_2.PasswordPositionalRequirement import PasswordPositionalRequirement
from utils import load, load_ints, file_processor

import logging

logging.basicConfig(level=logging.INFO)

processed = [{
    'process': file_processor(day_1.process),
    'parts': [{
        'kwargs': {
            'data': load_ints('day_1/input.txt'),
        },
    }, {
        'kwargs': {
            'data': load_ints('day_1/input.txt'),
            'entry_count': 3
        }
    }],
}, {
    'process': file_processor(day_2.process),
    'parts': [{
        'kwargs': {
            'data': load('day_2/input.txt')
        }
    }, {
        'kwargs': {
            'data': load('day_2/input.txt'),
            'requirement_classes': [PasswordPositionalRequirement]
        }
    }]
}, {
    'process': file_processor(day_3.process),
    'parts': [{
        'kwargs': {
            'data': load('day_3/input.txt'),
            'acceleration': (3, 1)
        },
    }, {
        'process': file_processor(day_3.process_multiple),
        'kwargs': {
            'data': load('day_3/input.txt'),
            'accelerations': [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        },
        'finalizer': prod
    }, ]
}]


def get_runs(process_definition):
    parts = process_definition.get('parts')
    if parts:
        for part in parts:
            yield {**process_definition, **part}
    else:
        yield process_definition


def get_definitions(day_index: int = -1, part_index: int = -1):
    if day_index and day_index > -1:
        process = {
            **processed[day_index - 1],
            'day': day_index
        }
        if part_index and part_index > -1:
            part = {
                **process['parts'][part_index - 1],
                'part': part_index
            }
            process['parts'] = [part]
        return [process]
    return processed


@click.command()
@click.option(
    '-d',
    '--day',
    help='The day of advent to run.',
    type=click.IntRange(1, len(processed) + 1),
)
@click.option(
    '-p',
    '--part',
    help='The part of the day of advent to run.',
    type=click.INT,
)
def main(day: int = -1, part: int = -1):
    filtered_processes = get_definitions(day, part)
    for day_index, process_definition in enumerate(filtered_processes):
        parts = get_runs(process_definition)
        day = process_definition.get('day', day_index + 1)
        for part_index, part_definition in enumerate(parts):
            part = part_definition.get('part', part_index + 1)
            logging.info(f'Running Day {day} - Part {part}')
            runtime = part_definition.get('process')
            result = runtime(
                *part_definition.get('args', []),
                **part_definition.get('kwargs', {})
            )
            finalizer = part_definition.get('finalizer')
            if finalizer:
                result = finalizer(result)
            logging.info(f'Results: {result}')


if __name__ == '__main__':
    main()

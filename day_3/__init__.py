import math
import typing
from itertools import tee

from day_3.logger import get_logger


def lines_with_y(data: typing.Iterable[str]):
    output = enumerate(data)
    for y, line in output:
        yield y, line.strip()


def log_line(line: str, x_pos: int, is_collision: bool, logger):
    line_width = len(line)
    expanded_line_with = math.ceil(x_pos + 1 / line_width) * line_width
    output_line = [line[index % line_width] for index in range(0, expanded_line_with)]

    if is_collision:
        output_line[x_pos] = '¥'
    else:
        output_line[x_pos] = '±'
    output = ''.join(output_line)
    logger.info(output)


def process(
        data: typing.Iterable[str],
        acceleration: tuple[int, int],
        # open_space: str = '.',
        tree_space: str = '#'
):
    collisions = 0
    y_lines = lines_with_y(data)
    x_acceleration, y_acceleration = acceleration
    # skip the first line since, thus starting in-motion
    next(y_lines)
    # start at the first space we move to
    x_pos = x_acceleration
    for y_pos, line in y_lines:
        if y_pos % y_acceleration == 0:
            line_width = len(line)
            space_index = x_pos % line_width
            current_space = line[space_index]
            is_collision = current_space == tree_space
            if is_collision:
                collisions += 1

            log_line(line, x_pos, is_collision, get_logger(x_acceleration, y_acceleration))
            # We move forward after collision check because we are starting the loop
            # after having already moved
            x_pos += x_acceleration

    return collisions


def process_multiple(
        data: typing.Iterable[str],
        accelerations: typing.List[tuple[int, int]],
        *args,
        **kwargs
):
    inputs = tee(data, len(accelerations));
    results = iter([process(data=input, acceleration=acceleration, *args, **kwargs)
                    for input, acceleration in zip(inputs, accelerations)])

    return results

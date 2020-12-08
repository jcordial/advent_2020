import logging
import os
from hashlib import sha1

loggers = {}


def make_logger(name):
    log_file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        f'logs/{name}.txt'
    )

    handler = logging.FileHandler(log_file_path)
    handler.setLevel(logging.INFO)
    day_3_logger = logging.getLogger(name)
    day_3_logger.setLevel(logging.INFO)
    day_3_logger.addHandler(handler)
    loggers[name] = day_3_logger
    day_3_logger.propagate = False
    return day_3_logger


def get_logger(x_accel, y_accel):
    name = f'{x_accel}_{y_accel}'

    return loggers.get(name) or make_logger(name)

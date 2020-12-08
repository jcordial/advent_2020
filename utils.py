import typing
from datetime import timedelta
from hashlib import sha1


def load(file_name: str) -> typing.TextIO:
    return open(file_name, mode='r')


def load_ints(file_name: str):
    for line in load(file_name):
        yield int(line)


def file_processor(work):
    def process(data: typing.Any, *args, **kwargs):
        result = work(data, *args, **kwargs)
        if hasattr(data, 'close'):
            data.close()
        return result

    return process

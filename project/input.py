#!/usr/bin/env python
import sys
from collections import namedtuple


FILES = {
    "s": 'data/small.in',
    "small": 'data/small.in',
    "m": 'data/medium.in',
    "medium": 'data/small.in',
    "b": 'data/big.in',
    "big": 'data/big.in',
}

TOMATO = 'T'
MUSHROOM = 'M'

Problem = namedtuple('Problem', 'height width min_ingredient max_size data')


def read_data_file(path):
    with open(path) as f:
        lines = f.readlines()
        height, width, min_ingredient, max_size = lines[0].split()

        data = [list(l[:-1]) for l in lines[1:]]

        problem = Problem(
            width=width,
            height=height,
            min_ingredient=min_ingredient,
            max_size=max_size,
            data=data
        )

    return problem


if __name__ == '__main__':
    assert len(sys.argv) == 2
    data_file = FILES[sys.argv[1]]
    pb = read_data_file(data_file)

    print(pb)

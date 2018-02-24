#!/usr/bin/env python
import sys
from collections import namedtuple


TOMATO = 'T'
MUSHROOM = 'M'


Problem = namedtuple('Problem', 'height width min_ingredient max_size data')


def read_data_file(path):
    with open(path) as f:
        lines = f.readlines()
        height, width, min_ingredient, max_size = lines[0].split()

        data = [list(l[:-1]) for l in lines[1:]]

        problem = Problem(
            width=int(width),
            height=int(height),
            min_ingredient=int(min_ingredient),
            max_size=int(max_size),
            data=data
        )

    return problem

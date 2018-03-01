#!/usr/bin/env python
from collections import namedtuple


Problem = namedtuple(
    'Problem',
    'rows cols n_vehicules n_rides bonus n_step data'
)


def read_file(path):
    with open(path) as data_file:
        r, c, v, t, b, s = map(int, data_file.readline().split())
        data = [
            list(map(int, line.rstrip().split()))
            for line in data_file.readlines()
        ]

    return Problem(
        rows=r, cols=c, n_vehicules=v, n_rides=t, bonus=b, n_step=s,
        data=data
    )


def main():
    problem = read_file('data/a_example.in')
    print(problem)


if __name__ == "__main__":
    main()

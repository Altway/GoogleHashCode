#!/usr/bin/env python
from collections import namedtuple


Problem = namedtuple(
    'Problem',
    'rows cols n_vehicules n_rides bonus n_step rides'
)

Ride = namedtuple(
    'Ride',
    'start_x start_y end_x end_y min_start max_arrival',
)


def read_file(path):
    with open(path) as data_file:
        r, c, v, t, b, s = map(int, data_file.readline().split())
        rides = []
        for line in data_file.readlines():
            sx, sy, ex, ey, min_s, max_e = map(int, line.rstrip().split())
            rides.append(
                Ride(
                    start_x=sx, start_y=sy,
                    end_x=ex, end_y=ey,
                    min_start=min_s, max_arrival=max_e
                )
            )

    return Problem(
        rows=r, cols=c, n_vehicules=v, n_rides=t, bonus=b, n_step=s,
        rides=rides,
    )


def main():
    problem = read_file('data/a_example.in')
    print(problem)


if __name__ == "__main__":
    main()

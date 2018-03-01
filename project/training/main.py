#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from input import read_data_file
from fixed_height import solve

def main():
    print("Starting Main")

    assert len(sys.argv) == 2
    input_file = sys.argv[1]

    problem = read_data_file(input_file)
    print('Width: {} / Height: {}'.format(problem.width, problem.height))

    all_slices = solve(problem)
    print(len(all_slices))
    for s in all_slices:
        print(' '.join(map(str, s)))

    return 0


if __name__=='__main__':
    return_code = main()

    sys.exit(return_code)

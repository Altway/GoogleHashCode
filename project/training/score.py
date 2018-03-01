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
Solution = namedtuple('Solution', 'slices_number data')


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

def read_output_file(path):
    with open(path) as f:
        lines = f.readlines()
        
        slices_number = lines[0]
        data = []
        for i in range(1,len(lines)):
            data.append(lines[i].strip('\n').split(" "))

        solution = Solution(
            slices_number=int(slices_number),
            data=data
        )

    return solution


###
### MAIN
###

if __name__ == '__main__':
    
    assert len(sys.argv) == 3
    data_file = FILES[sys.argv[1]]
    data_file_2 = FILES[sys.argv[2]]

    #data_file = "data\example.in"
    #data_file_2 = "data\solution.in"
    pb = read_data_file(data_file)
    sol = read_output_file(data_file_2)

#print(pb.data[1][4])
#print()
print("Nombre de part : " + str(sol.slices_number))
for i in range(sol.slices_number):
    string = ""
    for j in range(4):
        string += sol.data[i][j] 
    #print(string + str(1))

score = 0
for i in range(sol.slices_number):
    t_number = 0
    m_number = 0
    for l in range(int(sol.data[i][0]),int(sol.data[i][2])+1):
        for c in range(int(sol.data[i][1]),int(sol.data[i][3])+1):
            score += 1
            if pb.data[l][c] == "T":
                t_number += 1
            elif pb.data[l][c] == "M":
                m_number += 1

    print("SLICE " + str(i+1))
    print ("T : " + str(t_number)) 
    print ("M : " + str(m_number)) 
print("SCORE : " + str(score))
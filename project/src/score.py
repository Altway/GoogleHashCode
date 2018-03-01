#!/usr/bin/env python
import sys
from collections import namedtuple


FILES = {
    "a": 'data/a_example.in',
    "b": 'data/b_should_be_easy.in',
    "c": 'data/c_no_hurry.in',
    "d": 'data/d_metropolis.in',
    "e": 'data/e_high_bonus.in',
    "sa": 'data/a_solution.in',
    "sb": 'data/b_solution.in',
    "sc": 'data/c_solution.in',
    "sd": 'data/d_solution.in',
    "se": 'data/e_solution.in'
}

OPTION = {
	"-v" : "verbose",
	"verbose" : "verbose",
	"-fv" : "fuckingverbose",
	"fuckingverbose" : "fuckingverbose"
}

Problem = namedtuple(
    'Problem',
    'rows cols n_vehicules n_rides bonus n_step rides'
)
Ride = namedtuple(
    'Ride',
    'start_x start_y end_x end_y min_start max_arrival',
)
Solution = namedtuple('Solution', 'n_rides data')


def read_data_file(path):
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

def read_output_file(path):
    with open(path) as f:
        lines = f.readlines()

        n_rides = len(lines)

        data=[]
        for line in lines:
            data.append(line.split())

        solution = Solution(
            n_rides=int(n_rides),
            data=data
        )

    return solution


###
### MAIN
###

if __name__ == '__main__':
    
    #assert len(sys.argv) == 3
    data_file = FILES[sys.argv[1]]
    data_file_2 = FILES[sys.argv[2]]

    #data_file = "data\example.in"
    #data_file_2 = "data\solution.in"
    pb = read_data_file(data_file)
    sol = read_output_file(data_file_2)

allrides = []
numberOfVehicules = pb.n_vehicules

for vehicules in sol.data:
    string=""
    for ride in vehicules:
        string += ride + " "
    print (string)

if numberOfVehicules != len(sol.data):
    print"ERROR : [WRONG OUTPUT FORMAT] number of lines different from the number of vehicules in the input file"

for vehiculeIndex in range(len(sol.data)):
    vehicules = sol.data[vehiculeIndex]
    numberOfRides = int(vehicules[0])

    if numberOfRides != (len(vehicules)-1):
        print("ERROR : [VEHICULE {}] {} rides declared but {} rides really assigned".format(vehiculeIndex+1, numberOfRides, len(vehicules)-1))

    for i in range(numberOfRides+1):
        #print i
        if i != 0:
            if vehicules[i] in allrides:
                print("ERROR : [RIDE ASSIGNED MULTIPLES TIMES] RIDE {} is assigned more than one time".format(int(vehicules[i])))
                #assert vehicules[i] not in allrides
            allrides.append(vehicules[i])
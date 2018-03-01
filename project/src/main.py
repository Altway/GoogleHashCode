#!/usr/bin/env python
from collections import namedtuple


Problem = namedtuple(
    'Problem',
    'rows cols n_vehicules n_rides bonus n_step rides'
)


class Ride:
    def __init__(
            self, start_x, start_y, end_x, end_y,  min_start, max_arrival):

        self.start_x=start_x
        self.start_y=start_y
        self.end_x=end_x
        self.end_y=end_y
        self.min_start=min_start
        self.max_start=None
        self.max_arrival=max_arrival


class Car:
    def __init__(self):
        self.rides = []
        self.step = 0
        self.done = False


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
                    min_start=min_s,
                    max_arrival=max_e,
                )
            )

    return Problem(
        rows=r, cols=c, n_vehicules=v, n_rides=t, bonus=b, n_step=s,
        rides=rides,
    )


def distance(u, v):
    print(type(u))
    print(type(v))
    return abs(v[0] - u[0]) + abs(v[0] - u[0])


def sort_rides(ride):
    return ride.max_start


def choose_ride(car, pos, rides, step):
    for ride in rides:
        if ride.max_start < step:
            continue

        time_to_ride = distance(pos, (ride.start_x, ride.start_y)
        start_time = step + time_to_ride
        if start_time <= ride.max_start:
            
            return ride

    return None


def solve(problem):
    ride_sorting_strategy = sort_rides
    ride_selection_strategy = choose_ride

    for ride in problem.rides:
        dist = (ride.end_x - ride.start_x) + (ride.end_y - ride.start_y)
        ride.max_start = ride.max_arrival - dist - 1
    rides = sorted(problem.rides, key=ride_sorting_strategy)

    cars = [Car() for _ in range(problem.n_vehicules)]

    n_car_running = problem.n_vehicules
    while n_car_running:
        for car in cars:
            if car.done:
                continue

            if car.step > problem.n_step:
                car.done = True
                n_car_running -= 1

            current_pos = (car.rides[-1].end_x, car.rides[-1].end_y) if car.rides else (0, 0)

            best_ride = ride_selection_strategy(
                car, current_pos, rides, car.step
            )

            if not best_ride:
                car.done = True

            car.rides.append(best_ride)

            time = 
            car.step += distance((best_ride.), current_pos)


def main():
    problem = read_file('data/a_example.in')
    solve(problem)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
from collections import namedtuple

Problem = namedtuple(
    'Problem',
    'rows cols n_vehicules n_rides bonus n_step rides'
)


class Ride:
    def __init__(
            self, id_, start_x, start_y, end_x, end_y,  min_start, max_arrival):

        self.id = id_
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


def supervisor(problem, divider, cars):
    map_size = problem.rows * problem.cols
    


def read_file(path):
    with open(path) as data_file:
        r, c, v, t, b, s = map(int, data_file.readline().split())
        rides = []
        for id_, line in enumerate(data_file.readlines()):
            sx, sy, ex, ey, min_s, max_e = map(int, line.rstrip().split())
            rides.append(
                Ride(
                    id_=id_,
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
    return abs(v[0] - v[1]) + abs(u[0] - u[1])


def sort_rides(ride):
    return ride.max_start


def choose_ride(car, pos, rides, step, problem):
    index = None
    divider = problem.rows * problem.cols / 10
    for current_index, ride in enumerate(rides):
        
        if ride.max_start < step:
            continue
        
        time_to_ride = distance(pos, (ride.start_x, ride.start_y))
        if time_to_ride > divider:
            divider+=1
            continue
        start_time = step + time_to_ride

        if start_time <= ride.max_start:
            future_step = step + time_to_ride + distance(
                (ride.start_x, ride.start_y), (ride.end_x, ride.end_y)
            )
            if start_time < ride.min_start:
                future_step += ride.min_start - start_time

            index = current_index
            break

    if index is not None:
        ride = rides[index]
        rides = rides[:index] + rides[index+1:]
        return ride, future_step, rides

    return None, None, rides


def solve(problem):
    ride_sorting_strategy = sort_rides
    ride_selection_strategy = choose_ride

    for ride in problem.rides:
        dist = (ride.end_x - ride.start_x) + (ride.end_y - ride.start_y)
        ride.max_start = ride.max_arrival - dist - 1
    rides = sorted(problem.rides, key=ride_sorting_strategy)

    cars = [Car() for _ in range(problem.n_vehicules)]

    n_car_running = problem.n_vehicules
    while n_car_running > 0:
        for car in cars:
            if car.done:
                continue

            if car.step > problem.n_step:
                car.done = True
                n_car_running -= 1

            current_pos = (car.rides[-1].end_x, car.rides[-1].end_y) if car.rides else (0, 0)

            best_ride, future_step, rides = ride_selection_strategy(
                car, current_pos, rides, car.step, problem
            )

            if not best_ride:
                car.done = True
                n_car_running -= 1
            else:
                car.rides.append(best_ride)
                car.step = future_step

    return cars


def main():
    problem = read_file('data/e_high_bonus.in')
    cars = solve(problem)
    for car in cars:
        output = "{} {}".format(
            len(car.rides),
            ' '.join(map(str, [r.id for r in car.rides]))
        )
        print(output)


if __name__ == "__main__":
    main()

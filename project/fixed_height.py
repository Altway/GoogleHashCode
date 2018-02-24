from input import TOMATO, MUSHROOM


def slices(problem, height):
        for i in range(0, problem.height, height):
            r1, r2 = i, i+height-1
            yield problem.data[r1:r2+1], r1, r2

def solve(problem):

    slice_height = problem.max_size // 2
    print('Slice height: {}'.format(slice_height))

    all_slices = []

    for data, r1, r2 in slices(problem, slice_height):
   
        c1 = c2 = 0
        while c2 < problem.width:
            tomato = sum(
                1
                for ingredients in data
                for i in ingredients[c1:c2+1] if i == TOMATO
            )
            mushroom = sum(
                1
                for ingredients in data
                for i in ingredients[c1:c2+1] if i == MUSHROOM
            )
            if tomato >= problem.min_ingredient and mushroom >= problem.min_ingredient:
                all_slices.append((r1, c1, r2, c2))
                c2 += 1
                c1 = c2
            elif slice_height * (c2 - c1 + 1) > problem.max_size:
                #all_slices.append((r1, c1, r2, c1))
                c1 += 1
                c2 = c1
            else:
                c2 += 1

        if c1 != c2:
            c2 -= 1
            #all_slices.append((r1, c1, r2, c2))

    return all_slices

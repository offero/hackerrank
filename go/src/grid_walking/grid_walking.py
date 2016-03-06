#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/grid-walking

from collections import deque, defaultdict
from pprint import pprint


def findNumberOfPaths(position, dimensions, number_of_steps):
    """
    position: list/tuple. Coordinates of a single element (same size as
              dimensions).
    dimensions: list/tuple. Size of each dimension.
    """

    def neighbors(position):
        for dimension, dimension_size in enumerate(dimensions):

            if (position[dimension] + 1) < dimension_size:
                new_position = list(position)
                new_position[dimension] += 1
                yield tuple(new_position)

            if (position[dimension] - 1) >= 0:
                new_position = list(position)
                new_position[dimension] -= 1
                yield tuple(new_position)

    previous_step_values = defaultdict(lambda: 1)
    current_step_values = previous_step_values.copy()

    for number_of_steps in range(number_of_steps+1, 1, -1):

        positions_to_compute = deque([(position, number_of_steps)])
        while positions_to_compute:
            position_to_compute, steps = positions_to_compute.popleft()
            position_value = 0
            for neighbor in neighbors(position_to_compute):
                position_value += previous_step_values[neighbor]
                if (steps-1) > 0:
                    positions_to_compute.append((neighbor, steps-1))

            current_step_values[position_to_compute] = position_value

        previous_step_values, current_step_values = \
                current_step_values, previous_step_values

    pprint(previous_step_values)
    # pprint(current_step_values)
    return previous_step_values[position]


def main():
    number_of_test_cases = int(input().strip())
    for i in range(number_of_test_cases):
        number_of_dimensions, number_of_steps = tuple(map(int, input().strip().split()))
        # they provide coordinates as 1-based indexes. Convert it back.
        position = tuple(map(lambda x: int(x)-1, input().strip().split()))
        dimensions = tuple(map(int, input().strip().split()))
        print(findNumberOfPaths(position, dimensions, number_of_steps))


if __name__ == "__main__":
    main()
    # print(findNumberOfPaths((1, 2), (5, 7), 3))
    # findNumberOfPaths((0, 0), (2, 3), 3)

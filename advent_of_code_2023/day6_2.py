from typing import List

import requests
from icecream import ic

from advent_cookie import cookie

day = 6
mode = 11
if mode == 1:
    data = """
Time:      7  15   30
Distance:  9  40  200
""".strip()
else:
    data = requests.get(
        f"https://adventofcode.com/2023/day/{day}/input", cookies=cookie
    ).text


def parse_inputs(data: str) -> List[dict]:
    return_data = [{"time": "distance"}]
    lines = data.splitlines()
    times = [
        int(x) for x in lines[0].replace("Time:", "").strip().replace(" ", "").split()
    ]
    distances = [
        int(x)
        for x in lines[1].replace("Distance:", "").strip().replace(" ", "").split()
    ]
    for i in zip(times, distances):
        return_data.append({i[0]: i[1]})

    return return_data


input_data = parse_inputs(data)
print(input_data)


def multiply(list_of_inputs: List[int]) -> int:
    mult = 1
    for i in list_of_inputs:
        mult *= i
    return mult


def find_highers(list_of_inputs: List[int], target: int) -> int:
    highers = 0
    for i in list_of_inputs:
        if i > target:
            highers += 1
    return highers


def solve(input_data: List[dict]) -> int:
    """
    argument: dict(time=distance)
    how much hold, how fast you will be,
    """
    overall_combinations = []
    for input_dict in input_data:
        for time, distance in input_dict.items():
            ic(time, distance)
            # current_combinations = []
            start = 0
            end = 0
            for velocity in range(1, distance):
                left_time = time - velocity
                if left_time > 0:
                    possible_distance = velocity * left_time
                    if possible_distance > distance:
                        start = velocity
                        break
            # for velocity in range(distance, 1, -1):
            #     left_time = time - velocity
            #     # ic(velocity, left_time)
            #     if left_time > 0:
            #         possible_distance = velocity * left_time
            #         if possible_distance > distance:
            #             end = velocity
            #             break
                    # current_combinations.append(velocity * left_time)
            ic(start)
            # highers = find_highers(target=distance, list_of_inputs=current_combinations)
            # ic(highers, current_combinations)
            # overall_combinations.append(highers)
    # return multiply(overall_combinations)
            return time - start * 2 + 1

print(solve(input_data[1:]))

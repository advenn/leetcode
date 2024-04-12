import typing

import requests

cookie: str = ''
day = 5
mode = 11
if mode == 1:
    data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".strip()
else:
    data = requests.get(
        f"https://adventofcode.com/2023/day/{day}/input", cookies=cookie
    ).text


def parse_input(data):
    lines = data.split("\n")
    seeds = []
    maps = {
        "seed_to_soil_map": [],
        "soil_to_fertilizer_map": [],
        "fertilizer_to_water_map": [],
        "water_to_light_map": [],
        "light_to_temperature_map": [],
        "temperature_to_humidity_map": [],
        "humidity_to_location_map": [],
    }
    current_map = None

    for line in lines:
        if line.startswith("seeds:"):
            seed_ranges = map(int, line.split(":")[1].strip().split())
            for start, length in zip(seed_ranges, seed_ranges):
                seeds.append(range(start, start + length))
        elif "map:" in line:
            current_map = line.split(":")[0].replace("-", "_").strip().replace(" ", "_")
        elif line and current_map:
            start_dest, start_src, length = map(int, line.split())
            maps[current_map].append((start_dest, start_src, length))

    return seeds, maps


seeds, maps = parse_input(data)
print(seeds, maps)

def mapper(num, conversion_map):
    for start_dest, start_src, length in conversion_map:
        if start_src <= num < start_src + length:
            return start_dest + (num - start_src)
    return num  # Return the same number if it's not in the map


def find_lowest_location(seeds_: typing.List[int], maps_):
    lowest_location = float("inf")
    for seed in seeds_:
        soil = mapper(seed, maps_["seed_to_soil_map"])
        fertilizer = mapper(soil, maps_["soil_to_fertilizer_map"])
        water = mapper(fertilizer, maps_["fertilizer_to_water_map"])
        light = mapper(water, maps_["water_to_light_map"])
        temperature = mapper(light, maps_["light_to_temperature_map"])
        humidity = mapper(temperature, maps_["temperature_to_humidity_map"])
        location = mapper(humidity, maps_["humidity_to_location_map"])

        lowest_location = min(lowest_location, location)
    return lowest_location


lowest = []
for seed_list in seeds:
    cur_lowest = find_lowest_location(seed_list, maps)
    lowest.append(cur_lowest)
    print("Current lowest location number:", cur_lowest )

print(min(lowest))

# def parse_input(data):
#     lines = data.split('\n')
#     seed_ranges = []
#     maps = {
#         "seed_to_soil_map": [],
#         "soil_to_fertilizer_map": [],
#         "fertilizer_to_water_map": [],
#         "water_to_light_map": [],
#         "light_to_temperature_map": [],
#         "temperature_to_humidity_map": [],
#         "humidity_to_location_map": [],
#     }
#     current_map = None
#
#     for line in lines:
#         if line.startswith("seeds:"):
#             seed_values = map(int, line.split(':')[1].split())
#             seed_ranges = [(seed_values[i], seed_values[i+1]) for i in range(0, len(seed_values), 2)]
#         elif "map:" in line:
#             current_map = line.split(':')[0].replace('-', '_').replace(' ', '_').strip() + "_map"
#         elif line and current_map:
#             start_dest, start_src, length = map(int, line.split())
#             maps[current_map].append((start_dest, start_src, length))
#
#     return seed_ranges, maps
#
# def mapper(num, conversion_map):
#     for start_dest, start_src, length in conversion_map:
#         if start_src <= num < start_src + length:
#             return start_dest + (num - start_src)
#     return num
#
# def find_lowest_location(seed_ranges, maps):
#     lowest_location = float('inf')
#     for start, length in seed_ranges:
#         for seed in range(start, start + length):
#             soil = mapper(seed, maps["seed_to_soil_map"])
#             fertilizer = mapper(soil, maps["soil_to_fertilizer_map"])
#             water = mapper(fertilizer, maps["fertilizer_to_water_map"])
#             light = mapper(water, maps["water_to_light_map"])
#             temperature = mapper(light, maps["light_to_temperature_map"])
#             humidity = mapper(temperature, maps["temperature_to_humidity_map"])
#             location = mapper(humidity, maps["humidity_to_location_map"])
#             lowest_location = min(lowest_location, location)
#     return lowest_location
#
# # Replace with your actual data
# # data = """
# # ... (your puzzle input) ...
# # """
# seed_ranges, maps = parse_input(data)
# print("Lowest location number:", find_lowest_location(seed_ranges, maps))

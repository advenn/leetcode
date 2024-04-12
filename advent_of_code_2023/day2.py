from icecream import ic

lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
games = []
game = {}
count = 0
mode = "dcev"
if mode != "dev":
    lines = open("day2_input.txt", "r").read()
lines = lines.splitlines()
import re


def extract_game_ids(text):
    pattern = r"Game (\d+)"
    res = re.findall(pattern, text)
    if res:
        return int(res[0])
    return 0


limits = {"red": 12, "green": 13, "blue": 14}
# for line in lines:
#     game_id = extract_game_ids(line)
#     line = line.replace(f"Game {game_id}:", "")
#     parts = line.split(";")
#     game_parts = {}
#     for part in parts:
#         parts_ = part.split(",")
#         higher = False
#         # print(parts_)
#         for part_ in parts_:
#             c, color = part_.split()
#             ic(parts_, c, color, limits[color], int(c) > limits[color])
#
#             if int(c) > limits[color]:
#                 higher = True
#                 break
#         #     print(part_, parts_)
#         #     for color, value in game_parts.items():
#         #         if value > limits[color]:
#         #             higher = True
#         # if color not in game_parts.keys():
#         #     game_parts[color] = int(c)
#         # else:
#         #     game_parts[color] += int(c)
#         # if higher:
#         #     break
#         if not higher:
#             count += game_id
#         # ic(line, higher, count, )


# print(count)

for line in lines:  # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game_id = extract_game_ids(line)  # 1
    line = line.replace(
        f"Game {game_id}:", ""
    )  # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    parts = line.replace(";", ",").split(",")  # [3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green]
    higher = False

    for part in parts:  # 3 blue, 4 red
        c, color = part.split()
        # ic(line, parts, color, higher)
        if int(c) > limits[color]:
            higher = True
            break
        # break
    # ic(line, parts, part,part_, higher)
    if not higher:
        count += game_id

print(count)

vals = 0
for line in lines:  # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    currents = {}
    game_id = extract_game_ids(line)  # 1
    line = line.replace(
        f"Game {game_id}:", ""
    )  # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    parts = line.replace(";", ",").split(",")  # [3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green]
    higher = False

    for part in parts:  # 3 blue, 4 red
        c, color = part.split()
        # ic(line, parts, color, higher)
        if color in currents:
            if int(c) > currents[color] :
                currents[color] = int(c)
        else:
            currents[color] = int(c)
        # if int(c) > limits[color]:
        #     higher = True
        #     break
        # break
    # ic(line, parts, part,part_, higher)
    # if not higher:
    #     count += game_id
    if currents:
        current = 1
        for value in currents.values():
            current *= value
        vals += current

print(vals)
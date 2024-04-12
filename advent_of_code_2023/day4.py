import re

import requests
from icecream import ic

from advent_cookie import cookie


def extract_card_ids(text):
    res = text.split(":")[0]
    res = res.split()[1]
    if res:
        return int(res)


# test = ["Card   1: v", "Card   15: v","Card   34: v","Card   100: v","Card   1123: v","Card   112: v","Card   11234: v"]
# for t in test:
#     print(t,"|", extract_card_ids(t))
# exit()
mode = 11
if mode == 1:
    input4 = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip()
else:
    input4 = requests.get(
        "https://adventofcode.com/2023/day/4/input", cookies=cookie
    ).text

lines = input4.splitlines()
len_rows = len(lines)
matrix = [["", [j + 1 for j in range(len_rows)], ""]] + [
    [i, [0 for _ in range(len_rows)], 0] for i in range(1, len_rows + 1)
]
# matrix[1][1][0] = 1
ic(matrix)
# exit()
# part one
# chances = 0
# for line in lines:
#     card_id = extract_card_ids(line)
#     # ic(card_id)
#     line = line.split(":")[1]  #  line.replace(f"Card {card_id}:", "")
#     winning_nums = list(map(int, line.split("|")[0].split()))
#     my_nums = list(map(int, line.split("|")[1].split()))
#     winning_nums_I_own = set(winning_nums) & set(my_nums)
#     if len(winning_nums_I_own):
#         chances += 1 * (2 ** (len(winning_nums_I_own) - 1))

# ic(line, card_id, winning_nums, my_nums, winning_nums_I_own, chances)
# print(chances)


# part two
# cards = {1: 1}
#
# for line in lines:
#     card_id = extract_card_ids(line)
#     ic(card_id)
#     line = line.split(":")[1]  #  line.replace(f"Card {card_id}:", "")
#     winning_nums = list(map(int, line.split("|")[0].split()))
#     my_nums = list(map(int, line.split("|")[1].split()))
#     winning_nums_I_own = set(winning_nums) & set(my_nums)
#     num_of_w_nums = len(winning_nums_I_own)
#     ic(num_of_w_nums, winning_nums_I_own, cards)
#     for n in range(num_of_w_nums):
#         next_card = card_id + n + 1
#         ic(next_card, card_id)
#         if next_card not in cards.keys():
#             cards[next_card] = cards[card_id] + 1
#         else:
#             cards[next_card] += cards[card_id]
#     if not cards.get(card_id + 1):
#         if cards.get(card_id) > 1:
#             cards[card_id + 1] = 1
#         else:
#             break
#
# sum_cards = 0
# for k,v in cards.items():
#     sum_cards += v
# ic(cards, sum_cards)


for line in lines:
    card_id = extract_card_ids(line)
    line = line.split(":")[1]
    winning_nums = list(map(int, line.split("|")[0].split()))
    my_nums = list(map(int, line.split("|")[1].split()))
    num_of_w_nums = len(set(winning_nums) & set(my_nums))
    current_row = matrix[card_id]
    sum_row = sum(current_row[1])
    print(current_row[-1])
    matrix[card_id][-1] = num_of_w_nums
    for n in range(num_of_w_nums):
        next_card = card_id + n + 1
        next_card_details = matrix[next_card]
        next_card_details[1][card_id - 1] = sum_row  + 1
    if sum(current_row[1]) < 1 and num_of_w_nums == 0:
        break

print()
ic(matrix)
summ = 0
for row in matrix[1:]:
    summ += sum(row[1]) + 1

print(summ)
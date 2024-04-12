from icecream import ic

mode = "dfgev"
if mode == "dev":
    input3 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".strip()
else:
    input3 = open("day3_input", "r").read()

lines = input3.splitlines()
len_rows = len(lines)
len_row = len(lines[0])
summ = 0
nums_and_dot = [str(n) for n in range(10)] + ["."]
nums = []
#
# for current_line_index in range(len_rows):
#     current_num = ""
#
#     for char_index in range(len_row):
#         char = lines[current_line_index][char_index]
#         if not char.isdigit() or char_index == len_row - 1:
#             if current_num:
#                 if char.isdigit():
#                     current_num += char
#                 n_lines = [current_line_index]
#                 if current_line_index > 0:
#                     n_lines.append(current_line_index - 1)
#                 if current_line_index < len_rows - 1:
#                     n_lines.append(current_line_index + 1)
#                 len_current_char = len(current_num)
#                 indexes_on_line = [
#                     h
#                     for h in list(
#                         range(char_index - len_current_char - 1, char_index + 1)
#                     )
#                     if 0 <= h < len_row
#                 ]
#                 found = False
#                 for l in n_lines:
#                     for ind in indexes_on_line:
#                         ch = lines[l][ind]
#                         if ch not in nums_and_dot:
#                             summ += int(current_num)
#                             nums.append(int(current_num))
#                             found = True
#                             break
#                     if found:
#                         break
#                 ic(
#                     n_lines,
#                     len_current_char,
#                     indexes_on_line,
#                     current_num,
#                     current_line_index,
#                     summ,
#                 )
#                 current_num = ""
#             continue
#         if char.isdigit():
#             current_num += char
#         ic(current_num)
# print(summ, nums, sum(nums))

# part two
# part_two_sum = 0
# for current_line_index in range(len_rows):
#     current_num = ""
#     for char_index in range(len_row):
#         char = lines[current_line_index][char_index]
#         if char == "*":
#             n_lines = [current_line_index]
#             if current_line_index > 0:
#                 n_lines.append(current_line_index - 1)
#             if current_line_index < len_rows - 1:
#                 n_lines.append(current_line_index + 1)
#             len_current_char = len(current_num)
#             indexes_on_line = [
#                 h
#                 for h in list(range(char_index - len_current_char - 1, char_index + 2))
#                 if 0 <= h < len_row
#             ]
#             num1 = 0
#             num2 = 0
#             for l in n_lines:
#                 for ind in indexes_on_line:
#                     ch = lines[l][ind]
#                     if ch.isdigit():
#                         start_ind = ind
#                         end_ind = 0
#                         prev_check=False
#                         next_check=False
#                         prev_ind = ind
#                         next_ind = ind
#                         prev_char = ""
#                         next_char = ""
#                         while True:




neighbours = {}  #   "cli:char_index":[1,2]



for current_line_index in range(len_rows):
    current_num = ""

    for char_index in range(len_row):
        char = lines[current_line_index][char_index]
        if not char.isdigit() or char_index == len_row - 1:
            if current_num:
                if char.isdigit():
                    current_num += char
                n_lines = [current_line_index]
                if current_line_index > 0:
                    n_lines.append(current_line_index - 1)
                if current_line_index < len_rows - 1:
                    n_lines.append(current_line_index + 1)
                len_current_char = len(current_num)
                indexes_on_line = [
                    h
                    for h in list(
                        range(char_index - len_current_char - 1, char_index + 1)
                    )
                    if 0 <= h < len_row
                ]
                found = False
                for l in n_lines:
                    for ind in indexes_on_line:
                        ch = lines[l][ind]
                        if ch not in nums_and_dot and ch == "*":
                            if f"{l}:{ind}" not in neighbours.keys():
                                neighbours[f"{l}:{ind}"] = [int(current_num)]
                            else:
                                neighbours[f"{l}:{ind}"] += [int(current_num)]

                            # summ += int(current_num)
                            # nums.append(int(current_num))
                            found = True
                            break
                    if found:
                        break
                ic(
                    n_lines,
                    len_current_char,
                    indexes_on_line,
                    current_num,
                    current_line_index,
                    summ,
                )
                current_num = ""
            continue
        if char.isdigit():
            current_num += char
        ic(current_num)
print(neighbours)
two_sum = 0
for k,v in neighbours.items():
    if len(v ) ==2:
        two_sum += v[0]*v[1]
print(two_sum)
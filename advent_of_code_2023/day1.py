import typing

from icecream import ic



# part two
with open("day1_input.txt", "r") as f:
    input1 = f.read()

word2num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


lines = input1.splitlines()


# def word_to_num(string: str) -> str:
#     initials = tuple("efnost")
#     words = list(word2num.keys())
#     for index, char in enumerate(string):
#         if char in initials:
#             count_ = 1
#             while count_ < 6:
#                 w = string[index: index + count_]
#                 if w in words:
#                     ic(w, string,index, index + count_, string[index:] + str(word2num[w])+ string[:index + count_ + 1])
#                     break
#                 count_ += 1
def word_to_num(string: str) -> str:
    # Mapping of number words to their numeric equivalents
    word2num = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    # Start at the beginning of the string and look for number words
    index = 0
    while index < len(string):
        # Find the longest matching number word at the current position
        for length in range(
            5, 1, -1
        ):  # Assuming the longest word is 5 letters (e.g., "three")
            if index + length <= len(string):
                substring = string[index : index + length]
                if substring in word2num:
                    # Replace the number word with its numeric equivalent
                    string = (
                        string[:index] + word2num[substring] + string[index + length :]
                    )
                    index += len(word2num[substring]) - 1  # Move past the replacement
                    break
        index += 1

    return string


# Example usage
words = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]
# for w in words:
#     print(word_to_num(w))


# words = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".splitlines()
# for w in words:
#     word_to_num(w)


def count2(lines):
    vals = []
    for line in lines:
        ic(line)
        line = word_to_num(line)
        ic(line)
        num1 = None
        num2 = None
        line_len = len(line)

        for index in range(line_len):
            if line[index].isdigit():
                num1 = int(line[index])
                break
        for index in range(line_len - 1, -1, -1):
            if line[index].isdigit():
                num2 = int(line[index])
                break
        vals += [num1 * 10 + num2]
    return vals


def find_number(
    string, direction: typing.Literal["left", "right"], count_words: bool = False
) -> int:
    initials = tuple("efnost")
    word2num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    range_len = len(string)
    def return_num(range_obj):
        for index in range_obj:
            char = string[index]
            if char.isdigit():
                return int(char)
            if count_words:
                if char in initials:
                    for length in (3, 4, 5):
                        cur = string[index : index + length]
                        if cur in word2num.keys():
                            return word2num[cur]
    if direction == "left":
        return return_num(range(range_len - 1, -1, -1))
    return return_num(range(range_len))


vals = 0
for w in lines:
    r, l = find_number(w, direction="right", count_words=False), find_number(
        w, direction="left", count_words=False
    )
    vals += r * 10 + l

print(vals)

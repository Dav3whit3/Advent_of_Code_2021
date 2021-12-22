import sys
sys.path.append('../Advent_of_Code_2021')
from functools import reduce
from utils.tools import input_parser, current_stars



def parse_line(line, t="output"):

    parsed_line = line.split("|")[1].strip().split(" ")
    if t == "input":
        parsed_line = line.split("|")[0].strip().split(" ")
        parsed_line.sort(key=len)

    return parsed_line


def is_segment_unique(segment: str) -> bool:
    # True / False in output values
    return len(segment) in (2, 4, 3, 7)


def line_unique_segments(line: list) -> int:
    return reduce(lambda a, b: a+1,
                  filter(is_segment_unique, parse_line(line, t="output")), 0)  # Count of unique segments per line


def solution_part1(input: list) -> int:
    return reduce(lambda a, b: a+b,
                  map(line_unique_segments, input))  # Count of all unique segment throughout the given input




# Part 2
def decode(line: list) -> dict:
    key = {}
    count = {}

    for word in line:
        for letter in word:
            c = count.get(letter)
            count[letter] = 1 if c is None else count[letter] + 1

    for letter in count.keys():
        # tl = letter repeated 6x
        if count[letter] == 6:
            key["tl"] = letter

        # bl = letter repeated 3x
        elif count[letter] == 4:
            key["bl"] = letter

        # br = letter repeated 9x
        elif count[letter] == 9:
            key["br"] = letter

    # t = letter in word len 3 (7) not in word len 2 (1)
    for letter in line[1]:
        if letter not in line[0]:
            key["t"] = letter

    # tr = Unknown letter in word len 3 (7)
    for letter in line[1]:
        if letter not in key.values():
            key["tr"] = letter

    # m = Unknown letter in word len 4 (4)
    for letter in line[2]:
        if letter not in key.values():
            key["m"] = letter

    # b = Unknown letter in word len 7(8)
    for letter in line[-1]:
        if letter not in key.values():
            key["b"] = letter

    return key


def solve(line: str) -> int:

    input_values = parse_line(line, t="input")
    output_values = parse_line(line, t="output")

    key = decode(input_values)

    number = ""
    for word in output_values:
        if len(word) == 2:
            number += "1"
        elif len(word) == 3:
            number += "7"
        elif len(word) == 4:
            number += "4"
        elif len(word) == 7:
            number += "8"

        elif len(word) == 5:
            if key["bl"] in word:
                number += "2"
            elif key["tl"] in word:
                number += "5"
            else:
                number += "3"

        elif len(word) == 6:
            if key["m"] not in word:
                number += "0"
            else:
                if key["bl"] in word:
                    number += "6"
                else:
                    number += "9"
    return int(number)


def solution_part2(input: list) -> int:

    result = reduce(lambda a, b: a+b,
                    map(solve, input))

    return result


if __name__ == '__main__':

    example = [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ]

    input_08 = input_parser(day=8)
    print(f"Example Part 1: {solution_part1(example)}")
    print(f"Solution Part 1: {solution_part1(input_08)}")

    print(f"Example Part 2: {solution_part2(example)}")
    print(f"Solution Part 2: {solution_part2(input_08)}")
    print(current_stars())
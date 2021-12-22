import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, current_stars, open_exercise_instructions


def solution_part1(array: list,
                   pos={"forward": 0,
                        "up": 0,
                        'down': 0}) -> int:
    if array:
        move = array[0].split(" ")
        pos[move[0]] += int(move[1])
        array.pop(0)
        return solution_part1(array, pos)
    return pos['forward'] * abs((pos['up'] - pos['down']))


def solution_part2(array: list,) -> int:

    pos = {"d": 0,
           "h": 0,
           "a": 0}

    while len(array):

        sp = array[0].split(" ")
        sp[1] = int(sp[1])

        if sp[0] == 'down':
            pos['a'] += sp[1]
        elif sp[0] == 'up':
            pos['a'] -= sp[1]
        else:
            pos['h'] += sp[1]
            pos['d'] = pos['d'] + (pos['a'] * sp[1])
        array.pop(0)
    return pos['h'] * pos['d']


if __name__ == '__main__':

    day = 2
    open_exercise_instructions(day)
    data = input_parser(day=day)
    sys.setrecursionlimit(len(data) + 3)
    print(f"Example Part 1: {solution_part1(data)}")
    data = input_parser(day=day)
    print(f"Solution Part 2: {solution_part2(data)}")
    print(current_stars())

import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, current_stars, open_exercise_instructions

def solution_part1():
    pass

def solution_part2():
    pass


if __name__ == '__main__':

    day = 
    open_exercise_instructions(day)
    data = input_parser(day=day)
    sys.setrecursionlimit(len(data) + 3)
    print(f"Solution Part 1: {solution_part1(data)}")
    print(f"Solution Part 2: {solution_part2(data)}")
    print(current_stars())
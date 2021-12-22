import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
import numpy as np
from functools import reduce
from utils.tools import input_parser, current_stars


def c_reduce(arr, start_1, stop_1, start_2, stop_2):
    return reduce(lambda a, b: a+b, arr[start_2 : stop_2]) > reduce(lambda a, b: a+b, arr[start_1 : stop_1])


def solution_part2(d, counter=0):
    if len(d) >= 3:
        if c_reduce(d, 0, 3, 1, 4): # Custom function which returns Bool if next 3-element-window of the array is bigger than the current one
            counter += 1
        return solution_part2(d[1:], counter=counter)    
    return counter

def solution_part1(data):
    return reduce(lambda a, b: a+1 if b>0 else a+0, np.diff(data), 0)



if __name__ == '__main__':

    input_01 = input_parser(day=1)
    input_01 = list(int(elem) for elem in input_01)
    sys.setrecursionlimit(len(input_01)+4)
    print(f"Solution Part 1: {solution_part1(input_01)}")
    print(f"Solution Part 2: {solution_part2(input_01)}")
    print(current_stars())
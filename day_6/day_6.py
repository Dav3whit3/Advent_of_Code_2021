import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, post_answer, current_stars
from collections import deque
from functools import reduce


def day_6_input_transformer(inPut):

    sp = inPut[0].split(",")

    return list(int(elem) for elem in sp)


def fish_propagation(days, data):

    data = deque(reduce(lambda accum, val: accum+1 if val == unique else accum+0, data, 0) for unique in range(9))
    for d in range(days):
        data.rotate(-1)
        data[6] += data[8]
        c = reduce(lambda a,b: a+b, data)
    
    return c


if __name__ == '__main__':

    inPut = input_parser(day=6)
    day_6_input = day_6_input_transformer(inPut)
    print(fish_propagation(18, [3,4,3,1,2]))
    print(fish_propagation(80, day_6_input))
    print(fish_propagation(256, day_6_input))

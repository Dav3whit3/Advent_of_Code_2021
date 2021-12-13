import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, current_stars
from functools import reduce
import math



def solution(array, part=1, current_value=0, last_sum=math.inf):
    cost = summ_of_diffs(array, current_value, part)
    return solution(array, part, current_value+1, last_sum=cost) if cost < last_sum else last_sum


def summ_of_diffs(array, val, part=1):
    if part==2:
        return reduce(lambda a,b: a+b, map(lambda b: + factorial_summ(abs(b - val)), array))
    return reduce(lambda a,b: a+b, map(lambda b: + abs(b - val), array))


def factorial_summ(n):
    return reduce(lambda a,b: a+b, range(n+1))




if __name__ == '__main__':
    
    ex = [16,1,2,0,4,2,7,1,2,14]
    input_7 = input_parser(day=7, t="intlist")
    print(f"Example Part 1: {solution(ex)}")
    print(f"Example Part 2: {solution(ex, part=2)}")
    print(f"Solution Part 1: {solution(input_7)}")
    print(f"Solution Part 2: {solution(input_7, part=2)}")
    print(current_stars())
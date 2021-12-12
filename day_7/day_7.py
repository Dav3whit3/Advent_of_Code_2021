import sys
from typing import Generator
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, post_answer, current_stars
from collections import deque
from functools import reduce



def solution(arr: list, part=1) -> int:
    max_cost = summ_of_diffs(arr, max(arr), part)
    return is_lower(arr, part, last_sum=max_cost)


def is_lower(array: list, part=1, current_value=0, last_sum=0) -> int:
    cost = summ_of_diffs(array, current_value, part)
    return is_lower(array, part, current_value+1, last_sum=cost) if cost < last_sum else last_sum


def summ_of_diffs(arr: list, val: int, part=1) -> int:
    if part==2:
        return reduce(lambda a,b: a+b, ( factorial_summ(abs(i - val)) for i in arr) )    
    return reduce(lambda a,b: a+b, (abs(i - val) for i in arr))


def factorial_summ(n: int) -> int:
    return reduce(lambda a,b: a+b, range(n+1))







if __name__ == '__main__':
    
    ex = [16,1,2,0,4,2,7,1,2,14]
    input_7 = input_parser(day=7, t="intlist")
    print(f"Example Part 1: {solution(ex)}")
    print(f"Example Part 2: {solution(ex, part=2)}")
    print(f"Solution Part 1: {solution(input_7)}")
    print(f"Solution Part 2: {solution(input_7, part=2)}")
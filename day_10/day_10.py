import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, post_answer, current_stars
from functools import reduce


OPEN_CHARS = ["(", "<", "[", "{"]
CLOSED_CHARS = [")", ">", "]", "}"]


def solution(data, part=1):

    illegal_chars = []
    incomplete_scores = []

    for line in data:
        open_stack = []
        for char in line:
            if is_openening(char):
                open_stack.append(char)

            if is_closing(char):
                if pair_is_closed(open_stack[-1], char):
                    open_stack.pop(-1)
                else:
                    illegal_chars.append(char)
                    break
        else:
            complement = complement_stack(open_stack)
            incomplete_scores.append(part2_score(complement))
        
    if part == 1:
        return reduce(lambda a, b: a + score(b), illegal_chars, 0)

    l = len(incomplete_scores)
    middle_score = sorted(incomplete_scores)[ int(l/2) ]

    return middle_score




def pair_is_closed(start, end):
    return OPEN_CHARS.index(start) == CLOSED_CHARS.index(end)


def is_openening(c):
    return c in OPEN_CHARS


def is_closing(c):
    return c in CLOSED_CHARS


def complement_stack(open_stack):
    return list(reversed([CLOSED_CHARS[OPEN_CHARS.index(c)] for c in open_stack]))


def part2_score(complement):    
    return reduce(lambda a, b: 5 * a + score(b, part=2), complement, 0)



def score(char, part=1):
    if char == ")":
        return 3 if part == 1 else 1
    elif char == "]":
        return 57 if part == 1 else 2
    elif char == "}":
        return 1197 if part == 1 else 3
    elif char == ">":
        return 25137 if part == 1 else 4




if __name__ == '__main__':
    
    input_10 = input_parser(day=10)
    print(solution(input_10))
    print(solution(input_10, part=2))
    print(current_stars())


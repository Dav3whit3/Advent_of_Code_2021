import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, current_stars, open_exercise_instructions
from functools import reduce

def check_inner_point(matrix, x, y):

    point = matrix[x][y]
    return True if point < matrix[x][y-1] and point < matrix[x][y+1] and point < matrix[x-1][y] and point < matrix[x+1][y] else False


def low_points(matrix):

    result = []
    last_x = len(matrix) - 1
    last_y = len(matrix[0]) - 1

    for x, row in enumerate(matrix):
        for y, number in enumerate(row):
            if number == 2:
                pass
            if x == 0:
                if y == 0:  # Top-left corner
                    result.append(number) if number < matrix[0][1] and number < matrix[1][0] else None
                elif y == last_y:  # Top-right corner
                    result.append( number) if number < matrix[0][-2] and number < matrix[1][-1] else None
                else:  # In between
                    result.append(number) if number < matrix[x][y-1] and number < matrix[x][y+1] and number < matrix[x+1][y] else None

            elif x == last_x:
                if y == 0:  # Bottom-left corner
                    result.append( number) if number < matrix[-2][0] and number < matrix[-1][1] else None
                elif y == last_y:  # Bottom-right corner
                    result.append( number) if number < matrix[-1][-2] and number < matrix[-2][-1] else None
                else:  # In between
                    result.append(number) if number < matrix[x][y-1] and number < matrix[x][y+1] and number < matrix[x-1][y] else None

            else:  # Inner
                if y == 0:
                    result.append(number) if number < matrix[x-1][y] and number < matrix[x+1][y] and number < matrix[x][y+1] else None
                elif y == last_y:
                    result.append(number) if number < matrix[x-1][y] and number < matrix[x+1][y] and number < matrix[x][y-1] else None
                else:
                    is_lowest = check_inner_point(matrix, x, y)
                    result.append(number) if is_lowest else None

    return result


def solution_part1(data):

    lp = low_points(data)

    return reduce(lambda a,b: a+b+1, lp, 0)



def solution_part2():
    pass


if __name__ == '__main__':

    example = [
        2199943210,
        3987894921,
        9856789892,
        8767896789,
        9899965678,
    ]
    example = [[int(v) for v in str(n)] for n in example]

    day = 9
    # open_exercise_instructions(day)
    data = input_parser(day=day)
    data = [[int(val) for val in row] for row in data]
    print(f"Solution EXAMPLE: {solution_part1(example)}")
    print(f"Solution Part 1: {solution_part1(data)}")
    #print(f"Solution Part 2: {solution_part2(data)}")
    print(current_stars())

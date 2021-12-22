
import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, post_answer, current_stars
import numpy as np


def boards_setup(input, lst=[]):

    ta = []
    for i in range(5):
        row = input[0].replace("  ", " ").split(" ")
        row = [int(n) for n in row if n != '']
        ta.append(row)
        input.pop(0)

    lst.append(ta)
    while input:
        return boards_setup(input)

    return lst


inPut = input_parser(day=4, double_el=True)
draw = inPut[0]
draw = [int(n) for n in draw.split(",")]
boards = boards_setup(inPut[1:])

TRACK = dict()
for boardNumber, bOaRd in enumerate(boards):
    TRACK[f'{boardNumber}'] = {
        "rows": {f"{rowPosition}": [] for rowPosition in range(5)},

        "cols": {f"{colPosition}": [] for colPosition in range(5)}
    }

def bingo_1():

    for draw_pos, draw_value in enumerate(draw):
        for numberOfBoard, board in enumerate(boards):
            for x, row in enumerate(board):
                for y, val in enumerate(row):
                    if draw_value == val:
                        TRACK[f'{numberOfBoard}']["rows"][str(x)].append((x, y))
                        TRACK[f'{numberOfBoard}']["cols"][str(y)].append((x, y))

                        row_counter = TRACK[f'{numberOfBoard}']["rows"]
                        if len(row_counter[str(x)]) == 5:
                            marked_rows = set(tup for key in row_counter.keys() for tup in row_counter[key])

                            UNMARKED_NUMBERS = 0
                            for i, rw in enumerate(board):
                                for j, vl in enumerate(rw):
                                    if (i, j) in marked_rows:
                                        continue
                                    UNMARKED_NUMBERS += vl

                            return UNMARKED_NUMBERS * draw_value


                        col_counter = TRACK[f'{numberOfBoard}']["cols"]
                        if len(col_counter[str(y)]) == 5:
                            marked_cols = set(tup for key in col_counter.keys() for tup in col_counter[key])

                            UNMARKED_NUMBERS = 0
                            for i, rw in enumerate(board):
                                for j, vl in enumerate(rw):
                                    if (i, j) in marked_cols:
                                        continue
                                    UNMARKED_NUMBERS += vl

                            return UNMARKED_NUMBERS * draw_value


def sum_unmarked_values(B):

    result = 0
    for r in B:
        for v in r:
            if not list(v.values())[0]:
                result += list(v.keys())[0]
    return result


def bingo_2():

    for board in boards:
        for x, row in enumerate(board[:5]):
            for y, val in enumerate(row):
                board[x][y] = {val: False}

    ACCUM_BOARDS = []

    for draw_value in draw:
        for b in boards:
            for x, row in enumerate(b[:5]):
                for y, val in enumerate(row):
                    key = list(b[x][y].keys())[0]
                    if draw_value == key:
                        b[x][y][key] = True
                        for k in range(5):
                            if all([dic_val for dic in b[k] for key_val, dic_val in dic.items()]) \
                            or all([dic_val for dic in np.transpose(b)[k]for key_val, dic_val in dic.items()]):
                                if b not in ACCUM_BOARDS:
                                    ACCUM_BOARDS.append(b)
                                    if len(ACCUM_BOARDS) == 100:
                                        return sum_unmarked_values(b) * draw_value

if __name__ == '__main__':
    print(bingo_1())
    print(bingo_2())



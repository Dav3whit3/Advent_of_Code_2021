import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from tqdm import tqdm
from utils.tools import input_parser, post_answer, current_stars


def input_wrangler(lst, simple=False):

    result = []

    for elem in lst:
        sp = elem.split(" -> ")
        f = sp[0].split(",")
        s = sp[1].split(",")
        x1, y1 = f[0], f[1]
        x2, y2 = s[0], s[1]
        
        if simple:
            if x1 == x2 or y1 == y2:
                result.append([int(x1), int(y1), int(x2), int(y2)])
        else:
            result.append([int(x1), int(y1), int(x2), int(y2)])


    return result


def day_5(data, full=False):

    SET_TRACK = set()
    SET = set()

    for elem in tqdm(data):
        
        x1, y1, x2, y2 = elem[0], elem[1], elem[2], elem[3]
        if full:
            diff_x = abs(x1 - x2)
            diff_y = abs(y1 - y2)

            if diff_x == diff_y:

                start_x = x1 if x1 < x2 else x2
                start_y = y1 if x1 < x2 else y2
                end_y = y2 if x1 < x2 else y1

                if (x1 == y1 and x2 == y2) or start_y < end_y:
                    for i in range(diff_x + 1):
                        coords = (start_x + i , start_y + i)
                        if coords in SET_TRACK:
                            SET.add(coords)
                        SET_TRACK.add(coords)


                elif x1 != y1 or x2 != y2:
                    if end_y < start_y:
                        for i in range(diff_x + 1):
                            coords = (start_x + i, start_y - i)
                            if coords in SET_TRACK:
                                SET.add(coords)
                            SET_TRACK.add(coords)

        if y1 == y2:
            inner = abs(x1 - x2) + 1
            m = min(x1, x2)

            for i in range(inner):
                coords = (m+i, y2)
                if coords in SET_TRACK:
                    SET.add(coords)
                SET_TRACK.add(coords)

        elif x1 == x2:
            inner = abs(y1 - y2) + 1
            m = min(y1, y2)
            for i in range(inner):
                coords = (x1, m+i)
                if coords in SET_TRACK:
                    SET.add(coords)
                SET_TRACK.add(coords)
                         
    return len(SET)




if __name__ == '__main__':

    inPut = input_parser(day=5)

    part_1_input = input_wrangler(inPut, simple=True)
    part_2_input = input_wrangler(inPut)

    part_1_result = day_5(part_1_input)
    part_2_result = day_5(part_2_input ,full=True)

    print(f"{part_1_result=}")
    print(f"{part_2_result=}")

    print(current_stars())


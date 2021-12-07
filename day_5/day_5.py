import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, post_answer, current_stars
from tqdm import tqdm


def input_wrangler(lst, simple=False):

    result = []

    for elem in lst:
        sp = elem.split(" -> ")
        if simple:
            f = sp[0].split(",")
            s = sp[1].split(",")
            x1, y1 = f[0], f[1]
            x2, y2 = s[0], s[1]

            if x1 == x2 or y1 == y2:
                result.append([int(x1), int(y1), int(x2), int(y2)])
        else:
            result.append(f"{sp[0]},{sp[1]}")

    return result


def part_1(data):

    result = list()
    SET = set()

    for i, elem in enumerate(tqdm(data)):
        if elem[1] == elem[3]:
            inner = abs(elem[0] - elem[2]) + 1
            m = min(elem[0], elem[2])

            for i in range(inner):
                coords = (m+i, elem[3])
                if coords in result:
                    SET.add(coords)
                result.append(coords)

        elif elem[0] == elem[2]:
            inner = abs(elem[1] - elem[3]) + 1
            m = min(elem[1], elem[3])
            for i in range(inner):
                coords = (elem[0], m+i)
                if coords in result:
                    SET.add(coords)

                result.append(coords)

    return len(SET)




def part_2(data):

    for i, elem in enumerate(tqdm(data)):
        print(f"Checking element {elem} -> {i+1} / {len(data)}")

    pass






if __name__ == '__main__':
    example = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
        "2,9 -> 2,9"
    ]
    print(current_stars())
    EXAMPLE = input_wrangler(example, simple=True)
    inPut = input_parser(day=5)
    simple_input = input_wrangler(inPut, simple=True)
    complex_input = input_wrangler(inPut)
    print(part_1(simple_input))
    print(part_1(EXAMPLE))

    part_2(complex_input)



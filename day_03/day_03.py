import sys
sys.path.append('/Users/davidblanco/Documents/personal/Advent_of_Code_2021')
from utils.tools import input_parser, current_stars, open_exercise_instructions

def solution_part1(array):
    b_len = len(array[0])
    n = len(array) // 2 + 1
    print(n)

    gamma_rate = ''
    epsilon_rate = ''
    for bit in range(b_len):
        ones = 0
        zeros = 0
        for bin in array:
            if bin[bit] == '1':
                ones+=1
            else:
                zeros+=1
            if ones >= n or zeros >= n:
                break
        if ones > zeros:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    print(f"{gamma_rate=} , {epsilon_rate=} ---> {int(gamma_rate, 2)=} , {int(epsilon_rate, 2)=}")
    return str(int(gamma_rate, 2) * int(epsilon_rate, 2))



def solution_part2(array, type, index=0):
    while len(array) > 1:

        count = {
            "0": 0,
            "1": 0
        }

        for bin in array:
            count[bin[index]] += 1
        
        if type == 'oxygen':
            if count["1"] > count["0"]:
                array = [elem for elem in array if elem[index] == '1']
            elif count["0"] > count["1"]:
                array = [elem for elem in array if elem[index] == '0']
            else:
                array = [elem for elem in array if elem[index] == '1']

            index += 1
            if index == 12:
                index = 0
            return solution_part2(array=array, type=type, index=index)

        elif type == 'co2':
            if count["1"] > count["0"]:
                array = [elem for elem in array if elem[index] == '0']
            elif count["0"] > count["1"]:
                array = [elem for elem in array if elem[index] == '1']
            else:
                array = [elem for elem in array if elem[index] == '0']

            index += 1
            if index == 12:
                index = 0
            return solution_part2(array=array, type=type, index=index)

    result = int(array[0], 2)
    
    return result


if __name__ == '__main__':

    day = 3
    open_exercise_instructions(day)
    data = input_parser(day=day)
    sys.setrecursionlimit(len(data) + 3)
    print(f"Solution Part 1: {solution_part1(data)}")
    oxygen = solution_part2(data, "oxygen")
    co2 = solution_part2(data, "co2")
    print(f"Solution Part 2: {oxygen*co2}")
    print(current_stars())
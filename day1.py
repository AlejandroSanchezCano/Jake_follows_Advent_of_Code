'''
Welcome to Advent of Code! 
Day 1: Calorie Counting
https://adventofcode.com/2022/day/1
'''

import argparse
import numpy as np

def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = 'https://adventofcode.com/2022/day/1'
        )
    parser.add_argument(
        'input', 
        type = str,
        help = "List of calories carried by each elf. A blank line is an "\
        "indication of the reparation between each elf's calorie list")
    args = parser.parse_args()
    return args


def calorie_counter(input_url:str) -> tuple[int, int]:
    '''
    ### INPUT ###
    1) input_url = input file url
    ### OUTPUT ###
    1) Calorie amount of the elf with more calories
    2) Calorie amount of the 3 elves with more calories
    ### FUNCTION ###
    Reads the input file by line. If the line is a calorie number, sums it to 
    the elf's count of calories (last element of a list). Else, create new
    element in array with 0 calories
    '''
    
    with open(input_url) as input_file:
        calories_per_elf = np.array([0])
        for calorie_line in input_file.readlines():
            if calorie_line == '\n':
                calories_per_elf = np.append(calories_per_elf, 0)
            else:
                calories_per_elf[-1] += int(calorie_line.rstrip('\n'))
    
    # np.argsort(array) to get the index of the n max elements in array
    sorted_elfs = np.argsort(calories_per_elf)
    elf_with_more_calories = sorted_elfs[-1]
    three_elves_with_more_calories = sorted_elfs[-3:]
    
    return (
        calories_per_elf[elf_with_more_calories],
        sum(calories_per_elf[three_elves_with_more_calories])
        )


def main():
    print(calorie_counter(argument_parser().input))


if __name__ == "__main__":
    main()
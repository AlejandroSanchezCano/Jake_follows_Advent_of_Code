'''
Welcome to Advent of Code! 
Day 3: Rucksack Reorganization
https://adventofcode.com/2022/day/3
'''

#### Unpack operators *, **, *_
#### * unpacking operator, you can use that to pass a list to function arguments
#### ord()
#### map(function, iter)
#### np.array_split()

import argparse
import numpy as np

parser = argparse.ArgumentParser(
    description = 'https://adventofcode.com/2022/day/3'
    )
parser.add_argument(
    'input', 
    type = str,
    help = 'Text file with each line containing the elements of each rucksack.'\
        'Half of them for the first compartment and the other half for the'\
        'second one.')
args = parser.parse_args()

def priority_calculator(letter:str) -> int:
    '''
    ### INPUT ###
    1) letter = a-zA-Z
    ### OUPUT ###
    1) Number assignated to each letter (a = 1, A = 27, Z = 52)
    ### FUNCTION ###
    Transform a letter into its corresponded "priority" number
    '''
    corrector = 38 if letter.isupper() else 96
    priority = ord(letter) - corrector
    return priority

def reorganization(input_url:str) -> int:
    '''
    ### INPUT ###
    1) input_url = input file url
    ### OUTPUT ###
    1) Priority number 1-52
    ### FUNCTION ###
    Reads the input line by line, split them in halves, get the common element
    of the halves and translate to the priority number of that common element
    '''
    with open(input_url) as rucksack_file:
        priorities = 0
        for rucksack in rucksack_file.readlines():
            # Get common element
            compartment_1 = set(rucksack[:len(rucksack)//2])
            compartment_2 = set(rucksack[len(rucksack)//2:-1])
            common_item, *_ = compartment_1.intersection(compartment_2)
            # Get priority
            priorities += priority_calculator(common_item)
            
        return priorities
    
def badge(input_url:str) -> int:
    '''
    ### INPUT ###
    1) input_url = input file url
    ### OUTPUT ###
    1) Priority number 1-52
    ### FUNCTION ###
    Reads the file by bits of 3 lines, finds the common element in those 3
    lines and translate it to the proprity number
    '''
    with open(input_url) as rucksack_file:
        priorities = 0
        # Get common element
        rucksack_lines = rucksack_file.read().split('\n')[:-1]
        for group in np.array_split(rucksack_lines, len(rucksack_lines)//3):
            common_item, *_ = set(group[0]) & set(group[1]) & set(group[2])
            # Get priority
            priorities += priority_calculator(common_item)
    return priorities

def main():
    print(reorganization(args.input))
    print(badge(args.input))

if __name__ == "__main__":
    main()
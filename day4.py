'''
Welcome to Advent of Code! 
Day 3: Camp Cleanup
https://adventofcode.com/2022/day/4
'''

import re
import argparse
import numpy as np

parser = argparse.ArgumentParser(
    description = 'https://adventofcode.com/2022/day/4'
    )
parser.add_argument(
    'input', 
    type = str,
    help = 'Text file with each line containing the tasks of each elf pair in'\
        'the following format: 1-4, 2-8 = each pair of numbers indicates the'\
        'range of tasks per elf.'
        )
args = parser.parse_args()

def complete_overlap(elf1, elf2):
    if elf1.difference(elf2) == set() or elf2.difference(elf1) == set():
        return True
    else:
        return False

def partial_overlap(elf1, elf2):
    if elf1.intersection(elf2) != set():
        return True
    else:
        return False

def task_overlap(input_url:str) -> int:
    with open(input_url) as tasks_file:
        overlap_counter = [0,0]
        for elvan_pair in tasks_file.readlines():
            # Get the 4 numbers
            tasks = re.split(r'[,-]', elvan_pair.rstrip('\n'))
            # Convert 4 numbers to array of int
            tasks = np.array(tasks).astype(int)
            # Zip even and odd tasks and make them sets
            interval_to_set = lambda x: set(range(*x))
            elf1, elf2 = map(interval_to_set, zip(tasks[::2], tasks[1::2] + 1))
            # Calculate overlaps
            #print(elf1, elf2)
            overlap_counter[0] += complete_overlap(elf1, elf2)
            overlap_counter[1] += partial_overlap(elf1, elf2)
        return overlap_counter
            

def main():
    print(task_overlap(args.input))

if __name__ == "__main__":
    main()

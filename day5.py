'''
Welcome to Advent of Code! 
Day 5: Supply stacks
https://adventofcode.com/2022/day/1
'''

import re
import argparse
import numpy as np

parser = argparse.ArgumentParser(
    description = 'https://adventofcode.com/2022/day/1'
    )
parser.add_argument(
    'input', 
    type = str,
    help = "The input file contains the starting disposition and configuration "\
    "stack of crates and the rearrangement procedure by the crane "
    )
args = parser.parse_args()

def stack_crates(input_url:str, crane:int) -> str:
    '''
    ### INPUT ###
    1) input_url = input file url
    2) Type of crane
        - 9000 = the crates are moved one by one
        - 9001 = the crates are moved at the same time
    ### OUTPUT ###
    1) Array of strings representing the initial configuration of the stacks
    of crates
    ### FUNCTION ###
    Reads the input file by line. Transforms the stack configuration into a
    list of list, and performs the moves accroding to the instructions. Returns
    the top layer of crates
    '''
    with open(input_url) as input_file:
        arrangement = []
        for line in input_file.readlines():
            # Pick the letters/spaces by iterating over each 4th element on
            # the lines that contain crates
            if not line.startswith((' 1', '\n', 'move')):
                arrangement.append(list(line[1::4]))
            # At the empty line, make the initial configuration of the 
            # stack of crates by transposing and getting rid of the empty 
            # positions
            elif line.startswith('\n'):
                crates = np.array(arrangement).T.tolist()
                for i, stack in enumerate(crates):
                    crates[i] = [crate for crate in stack if crate != ' ']
            # Apply the moves
            elif line.startswith('move'):
                guide = list(map(int, re.findall(r'\d+', line)))
                if crane == 9000:
                    crates_taken = crates[guide[1] - 1][:guide[0]][::-1]
                elif crane == 9001:
                    crates_taken = crates[guide[1] - 1][:guide[0]]
                else: raise ValueError('Invalid crane argument value')
                
                crates[guide[1] - 1] = crates[guide[1] - 1][guide[0]:]
                crates[guide[2] - 1] = crates_taken + crates[guide[2] - 1]
    
    # Return top crates
    top = ''.join([crate[0] for crate in crates])
    return top

def main():
    print(stack_crates(args.input, 9000))
    print(stack_crates(args.input, 9002))


if __name__ == "__main__":
    main()
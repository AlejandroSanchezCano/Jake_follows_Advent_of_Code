'''
Welcome to Advent of Code! 
Day 6: Tuning trouble
https://adventofcode.com/2022/day/6
'''

import argparse

def argument_parser() -> argparse.Namespace():
    parser = argparse.ArgumentParser(
        description = 'https://adventofcode.com/2022/day/6'
        )
    parser.add_argument(
        'input', 
        type = str,
        help = "List of datastream buffers (string)")
    args = parser.parse_args()
    return args

def fix_comms(input_url:str, start_of:str) -> int:
    '''
    ### INPUT ###
    1) input_url = input file url
    ### OUTPUT ###
    1) Number of character that need to be processed to find the first
       substring with unique characters
    ### FUNCTION ###
    Reads the input file by line. Returns how many characters have to be 
    processed in each datastream buffer to find a marker
    '''
    if start_of != 4 and start_of != 14:
        raise ValueError('Invalid argument value. Only "packet" and "message"'\
                         'are valid values')
    with open(input_url) as datastream_file:
        for buffer in datastream_file.readlines():
            marker = set([])
            char = start_of
            while len(marker) != start_of:
                marker = set(buffer[char - start_of:char])
                char += 1
        return char - 1

def main():
    args = argument_parser()
    print(fix_comms(args.input, start_of = 4))
    print(fix_comms(args.input, start_of = 14))

if __name__ == "__main__":
    main()
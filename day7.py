'''
Welcome to Advent of Code! 
Day 7: No Space Left on Device
https://adventofcode.com/2022/day/7
'''

import argparse

#### os.system to run shell commands

def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = 'https://adventofcode.com/2022/day/7'
        )
    parser.add_argument(
        'input', 
        type = str,
        help = 'Command line commands and their output')
    args = parser.parse_args()
    return args

def filesystem(input_url:str) -> dict:
    '''
     ### INPUT ###
     1) input_url = input file url
     ### OUTPUT ###
     1) all_dir = dictionary with all the directory paths as keys and 
        directory size as values
     ### FUNCTION ###
     Reads the input file line by line. Goes over the commands and outputs
     to create a dictionary with all the directory paths as keys and 
     directory size as values
     
    '''
    all_dir = {'/':0}
    gwd = []
    with open(input_url) as cmd_line:
        for command in cmd_line.readlines():
            command = command.rstrip('\n').split(' ')
            if command[0] == '$' and command[1] == 'cd':
                # $ cd ..
                if command[2] == '..':
                    gwd = gwd[:-1]
                # cd directory
                else:
                    gwd.append(command[2])
            # dir directory
            elif command[0] == 'dir':
                path = '/'.join(gwd) + '/' + command[1]
                all_dir[path] = 0
            # size file
            elif command[0].isdigit():
                for n, directory in enumerate(gwd):
                    path = '/'.join(gwd[:n + 1])
                    all_dir[path] += int(command[0])

    return all_dir

def small_dir(all_dir:dict) -> int:
    '''
    ### INPUT ###
    1) all_dir =  dictionary with all the directory paths as keys and 
       directory size as values
    ### OUTPUT ###
    Size sum of directories with size <= 100000
    ### FUNCTION ###
    Filter directories with size <= 100000 and return their size sum
    '''
    return sum([size for size in all_dir.values() if size <= 100000])

def delete_dir(all_dir:dict) -> int:
    '''
    ### INPUT ###
    1) all_dir =  dictionary with all the directory paths as keys and 
       directory size as values
    ### OUTPUT ###
    Size of the directory with minimum size above the space to liberate cutoff
    ### FUNCTION ###
    Filter directories with size greater to the amount of space to liberate
    and return the directory with the smallest size above that cutoff
    '''
    to_remove = 30000000 - (70000000 - all_dir['/'])
    return min([size for size in all_dir.values() if size >= to_remove])

def main():
    print(small_dir(filesystem(argument_parser().input)))
    print(delete_dir(filesystem(argument_parser().input)))

if __name__ == "__main__":
    main()
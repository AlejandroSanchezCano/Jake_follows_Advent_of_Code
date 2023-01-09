'''
Welcome to Advent of Code! 
Day 10: Cathode-Ray Tube
https://adventofcode.com/2022/day/10
'''

import argparse

def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = 'https://adventofcode.com/2022/day/10'
        )
    parser.add_argument(
        'input', 
        type = str,
        help = 'Register commands'
        )
    args = parser.parse_args()
    return args

def show_image(register:list[int]) -> str:
    '''
    ### INPUT ###
    1) Register = register values
    ### OUTPUT ###
    1) screen = register translated into screen pixels
    ### FUNCTION ###
    Transforms the register into a 6 x 40 pixels screen CRT. If the cycle 
    matches the record value, a '#' is printed. Else,
    print '.'
    '''
    screen = ''
    pixels = list(range(40))*6
    for pixel, value in zip(pixels, register[:-1]):
        if pixel in (value - 1, value, value + 1):
            screen += '#'
        else:
            screen += '.'
            
    for row_init in range(0, len(screen), 40):
        print(screen[row_init:row_init + 40])
        
def signal_strength(register:list[int]) -> int:
    '''
    ### INPUT ###
    1) Register = register values
    ### OUTPUT ###
    1) Sum of the 20th, 60th ... 220th signal strength (cycle * register value)
    ### FUNCTION ###
    Computes the sum of the signal strenght for certain cycles.    
    '''
    cycles = [register[cycle - 1] * cycle for cycle in range(20, len(register), 40)]
    return sum(cycles)

def x_register(input_url:str):
    '''
    ### INPUT ###
    1) input_url = input file url
    ### OUTPUT ###
    1) register = register values
    ### FUNCTION###
    Computes the register values.
    '''
    # Compute register
    with open(input_url) as tick_program:
        commands = tick_program.readlines()
        register = [1]
        for command in commands:
            if command == 'noop\n':
                register.append(register[-1])
            else:
                addx = command.split(' ')[-1].rstrip('\n')
                register += [register[-1], register[-1] + int(addx)]
    
        return register
        
def main():
    print(signal_strength(x_register(argument_parser().input)))
    show_image(x_register(argument_parser().input))

if __name__ == "__main__":
    main()
    


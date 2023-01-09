'''
Welcome to Advent of Code! 
Day 11: Monkey in the Middle
https://adventofcode.com/2022/day/11
'''

#### everything needs to be optimized

import argparse
import numpy as np

def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = 'https://adventofcode.com/2022/day/11'
        )
    parser.add_argument(
        'input', 
        type = str,
        help = 'Notes about the monkey behaviour'
        )
    args = parser.parse_args()
    return args
    
def monkey_situation(input_url:str, stress_reduction = True) -> int:
    '''
    ### INPUT ###
    1) input_url = input file url
    2) stress_reduction = whether the stress levels drop after the monkey has 
    inspectioned the item
    ### OUTPUT ###
    1) monkey business
    ### FUNCTION ###
    Reads the file monkey by monkey, parses the monkey info and returns the
    monkey business (product of the amount of items have passed through the 
    two monkeys with the most items passed through).
    '''
    # Change parameters depending on the stress_reduction status
    cycles = 20 if stress_reduction else 10000
    div = 3 if stress_reduction else 1
    
    # Separate by monkeys
    monkeys = []
    for group in open(input_url).read().strip().split("\n\n"):
        lines = group.splitlines()
        monkey = []
        monkey.append(list(map(int, lines[1].split(": ")[1].split(", "))))
        monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
        for line in lines[3:]:
            monkey.append(int(line.split()[-1]))
        monkeys.append(monkey)
        
    # All tests numbers are primes, so we can reduce the numbers we get by
    # using the operation: value mod np.prod(primes)
    mod = int(np.prod(np.array([monkey[2] for monkey in monkeys])))
    
    # Execute cycles 
    counts = np.zeros(len(monkeys))
    for _ in range(cycles):
        for index, monkey in enumerate(monkeys):
            counts[index] += len(monkey[0])
            for item in monkey[0]:
                item = monkey[1](item) // div
                item %= mod
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            # Clear the monkey objects
            monkey[0] = []
    
    return np.prod(np.sort(counts)[-2:])
    
def main():
    print(monkey_situation(argument_parser().input, stress_reduction = True))
    print(monkey_situation(argument_parser().input, stress_reduction = False))

if __name__ == "__main__":
    main()
    
    
    
    
    
    

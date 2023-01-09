'''
Welcome to Advent of Code! 
Day 9: Rope Bridge
https://adventofcode.com/2022/day/9
'''

######match case for python > 3.10
##### don't initialize with [[]]*int, they are the same object
##### UNFINISHED

import argparse

def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = 'https://adventofcode.com/2022/day/9'
        )
    parser.add_argument(
        'input', 
        type = str,
        help = 'Series of motions indicating where does the head of the rope'\
            'moves (R - right, D - down, L - left, U - up)'
        )
    args = parser.parse_args()
    return args

def head_touches_tail(head:tuple[int,int], tail:tuple[int,int]) -> bool:
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        return False
    else:
        return True

def two_knots(input_url:str) -> int:
    head, tail = [(0,0)], [(0,0)]
    with open(input_url) as commands:
        for command in commands.read().split('\n')[:-1]:
            direction, steps = command.split(' ')
            for step in range(int(steps)):
                
                # Move head
                old = head[-1]
                if direction == 'L':
                    head.append((old[0], old[1] - 1))
                elif direction == 'R':
                    head.append((old[0], old[1] + 1))
                elif direction == 'U':
                    head.append((old[0] + 1, old[1]))
                else:
                    head.append((old[0] - 1, old[1]))
                    
                # Recalculate tail
                if head_touches_tail(head[-1], tail[-1]):
                    tail.append(tail[-1])
                else:
                    tail.append(old)
    return len(set(tail))

def ten_knots(input_url:str) -> int:
    with open(input_url) as commands:
        knots = [[(0, 0)] for i in range(10)]
        
        for command in commands.read().split('\n')[:-1]:
            direction, steps = command.split(' ')
            for step in range(int(steps)):
                
                # Move head
                old = knots[0][-1]
                if direction == 'L':
                    knots[0].append((old[0], old[1] - 1))
                elif direction == 'R':
                    knots[0].append((old[0], old[1] + 1))
                elif direction == 'U':
                    knots[0].append((old[0] + 1, old[1]))
                else:
                    knots[0].append((old[0] - 1, old[1]))
                    
                # Recalculate other knots
                for i in range(1, len(knots)):
                    if head_touches_tail(knots[i - 1][-1], knots[i][-1]):
                        knots[i].append(knots[i][-1])
                    else:
                        knots[i].append(knots[i - 1][-2])
    return len(set(knots[-1]))

def main():
    print(two_knots(argument_parser().input))
    print(ten_knots(argument_parser().input))


if __name__ == "__main__":
    main()

knots = [[(0, 0)],
 [(0, 0)],
 [(0, 0)],
 [(0, 0)],
 [(0, 0)],
 [(0, 0)],
 [(0, 0)],
 [(0, 0)],
 [(0, 0)],
 [(0, 0)]]

knots == [[(0,0)]]*10


'''
Welcome to Advent of Code! 
Day 12: Hill Climbing Algorithm
https://adventofcode.com/2022/day/12
'''

#### ord() is opposite of chr()

import argparse
import numpy as np

def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = 'https://adventofcode.com/2022/day/12'
        )
    parser.add_argument(
        'input', 
        type = str,
        help = ''
        )
    args = parser.parse_args()
    return args

def find_start(altitude_map):
    '''Finds start position in the map.'''
    start_index = np.where(altitude_map == 'S')
    coordinates = (start_index[0][0], start_index[1][0])
    return coordinates

def climbing_distance(point_a, point_b):
    '''Calculates distance between two points and indicates the direction to 
    take to get from point A to point B.'''
    xB_xA = point_b[0] - point_a[0]
    yB_yA = point_b[1] - point_a[1]
    distance = abs(xB_xA) + abs(yB_yA)
    direction = ['', '']
    if xB_xA > 0:
        direction[0] = 2
    elif xB_xA < 0:
        direction[0] = 0

    
    if yB_yA > 0:
        direction[1] = 1
    elif yB_yA < 0:
        direction[1] = 3
        
    return distance, direction

def move(
        altitude_map:np.array, 
        position:tuple, 
        good_directions:set, 
        possibilities:list
        ) -> tuple:
    '''Executes move.'''
    moves = {
        0: (lambda x: (x[0] - 1, x[1])), # UP
        1: (lambda x: (x[0], x[1] + 1)), # RIGHT
        2: (lambda x: (x[0] + 1, x[1])), # DOWN
        3: (lambda x: (x[0], x[1] - 1))  # LEFT
        }
    
    # good_directions = {2, 3}
    # possibilities = ['b', 'r', 'c','b']
    
    # Choose E or higher character if found
    current_state = altitude_map[position]
    next_state = chr(ord(current_state) + 1)
    if 'E' in possibilities and current_state == 'z':
        index_E = possibilities.index('E')
        return moves[index_E](position)
    elif next_state in possibilities:
        index_towards = possibilities.index(next_state)
        return moves[index_towards](position)
    # Choose equal character
    equal_indeces = [index for index, character in enumerate(possibilities)
             if character == current_state]
    for equal_index in equal_indeces:
        if equal_index in good_directions:
            return moves[equal_index](position)
        
    
def ascend_d_z(altitude_map, position):
    '''Calculates the distance between the current point and the points
    containing a higher character, chooses the closest ones and determines
    what are the directions to take to get to them'''
    current_state = altitude_map[position]
    next_state = chr(ord(current_state) + 1)
    next_state_positions = np.where(altitude_map == next_state)
    next_state_positions = list(zip(*next_state_positions))
    distances, directions = list(zip(*[climbing_distance(position, possibility)
                            for possibility in next_state_positions]))
    good_directions = [directions[index] for index in range(len(distances))
                   if distances[index] == max(distances)]
    # Flat array
    return set(np.array(good_directions).flatten().tolist())
    
    
def look_around(altitude_map, position):
    '''Returns the characters up, right, down and left from the current
    position.'''
    x, y = position
    up = lambda x, y: altitude_map[x - 1, y] if x - 1 > 0 else '1'
    down = lambda x, y: altitude_map[x + 1, y] if x + 1 < altitude_map.shape[0] else '1'
    left = lambda x, y: altitude_map[x, y - 1] if y - 1 > 0 else '1'
    right = lambda x, y: altitude_map[x, y + 1] if y + 1 < altitude_map.shape[1] else '1'
    moves = np.array([up(x, y), right(x, y), down(x, y), left(x, y)])
    
    return moves.tolist()



def climb_hill(input_url:str):
    with open(input_url) as altitude_file:
        altitude_rows = altitude_file.read().split('\n')[:-1]
        altitude_map = np.array([list(row) for row in altitude_rows])
    
    current = (1,7)#find_start(altitude_map)
    while altitude_map[current] != 'E':
        current = move(
            altitude_map,
            current,
            ascend_d_z(altitude_map, current),
            look_around(altitude_map, current)
            )
        print(altitude_map[current])

def main():
    print(climb_hill(argument_parser().input))

if __name__ == "__main__":
    main()
    
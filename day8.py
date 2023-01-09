'''
Welcome to Advent of Code! 
Day 8: Treetop Tree House
https://adventofcode.com/2022/day/8
'''

import argparse
import numpy as np

######np.vstack to append rows to matrix
##### print('\a') to play bell sound

def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = 'https://adventofcode.com/2022/day/8'
        )
    parser.add_argument(
        'input', 
        type = str,
        help = 'Grid of 0-9 numbers where each number represents a tree of the '\
        'patch and the value represents the tree height')
    args = parser.parse_args()
    return args


def tree_house(input_url:str) -> tuple[int, int]:
    '''
    ### INPUT ###
    1) input_url = input file url
    ### OUTPUT ###
    1) Sum of grid's visible trees from the outside
    2) Scenic score, calculated as
    ### FUNCTION ###
    Transforms the grid into a numpy array 2x2 and calculate each tree
    visibility (True if all tree up, down, left and right are smaller) and 
    scenic score (calculated as the multiplication of the amount to trees it
    can see)
    '''
    with open(input_url) as tree_file:
        # Transform grid into numpy matrix
        tree_patch = tree_file.read().split('\n')[:-1]
        digitalizer = lambda x:  list(map(int, x))
        tree_patch = list(map(digitalizer, tree_patch))
        tree_matrix = np.array(tree_patch)
        # Calculate visibility and scenic score
        visibility = np.ones(tree_matrix.shape)
        scenic_score = np.zeros(tree_matrix.shape)
        for i in range(1, tree_matrix.shape[0] - 1):
            for j in range(1, tree_matrix.shape[1] - 1):
                top = tree_matrix[0 : i, j] 
                down = tree_matrix[i + 1 : tree_matrix.shape[0], j]
                left = tree_matrix[i, 0 : j]
                right = tree_matrix[i, j + 1 : tree_matrix.shape[1]]
                
                # Calculare visibility
                visible = any([tree_matrix[i, j] > k 
                           for k in map(max, (top, down, left, right))])
                visibility[i, j] = int(visible)
                
                # Calculate scenic score
                directions = top[::-1], down, left[::-1], right           
                scenic_score_tree = np.full(4, list(map(len, directions)))
                for d, direction in enumerate(directions):
                    for t, tree in enumerate(direction):
                        if tree >= tree_matrix[i, j]:
                            scenic_score_tree[d] = t + 1
                            break
                scenic_score[i, j] = np.prod(scenic_score_tree)

        return sum(sum(visibility)), max(map(max, scenic_score))

def main():
    print(tree_house(argument_parser().input))

if __name__ == "__main__":
    main()
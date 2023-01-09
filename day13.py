'''
Welcome to Advent of Code! 
Day 13: Distress Signal
https://adventofcode.com/2022/day/13
'''

# import argparse
import numpy as np
# from typing import * 

# def argument_parser() -> argparse.Namespace:
#     parser = argparse.ArgumentParser(
#         description = 'https://adventofcode.com/2022/day/13'
#         )
#     parser.add_argument(
#         'input', 
#         type = str,
#         help = ''
#         )
#     args = parser.parse_args()
#     return args
def formatt(pair):
    # Enlist
    pair = [[i] if not isinstance(i, list) else i for i in pair]
    # Add 0
    max_length = max(map(len, pair))
    pair = [i + [0]*(max_length - len(i)) for i in pair]
    return pair

def compare(pair):
    if pair[0] > pair[1]:
        return False
    elif pair[0] < pair[1]:
        return True

def iteration(pair):
    for sub_pair in zip(*pair):
        if all([isinstance(i, int) for i in sub_pair]):
            print(sub_pair, '11111')
            if compare(sub_pair) != None:
                break
        else:
            print(sub_pair, '22222')
            sub_pair = formatt(sub_pair)
            iteration(sub_pair)
    
    return compare(sub_pair)

a = iteration([[1,1,3,1,1], [1,1,5,1,1]])
b = iteration([[[1],[2,3,4]], [[1],[4]]])
c = iteration([[9], [[8,7,6]]])
d = iteration([[[4,4],4,4], [[4,4],4,4,4]])
e = iteration([[1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]])






with open('test.txt') as distress_signal:
    for n, packet_pair in enumerate(distress_signal.read().rstrip().split('\n\n')):
        pair = list(map(eval, packet_pair.split('\n')))
        print(pair)

with open('day13.txt') as distress_signal:
    for n, packet_pair in enumerate(distress_signal.read().rstrip().split('\n\n')):
        pair = list(map(eval, packet_pair.split('\n')))
        print(np.array(pair[0]).flatten())
        print(np.array(pair[1]).flatten())
        print('-------')
        break
    
    
    
    
    
    
import sys, functools

def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a == b else (-1 if a < b else 1)
    a = [a] if isinstance(a, int) else a
    b = [b] if isinstance(b, int) else b
    return ([cmp(*p) for p in zip(a, b) if cmp(*p) != 0] + [cmp(len(a), len(b))])[0]

with open('test.txt') as fff:
    lists = [eval(a) for a in fff.read().strip().replace("\n\n", "\n").split("\n")]
print(sum(i for i, pair in enumerate(zip(lists[::2], lists[1::2]), 1) if cmp(*pair) <= 0))   

new = sorted(lists + [[[2]], [[6]]], key=functools.cmp_to_key(cmp))
print((new.index([[2]]) + 1) * (new.index([[6]]) + 1))

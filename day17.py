import numpy as np
# List of gas
gases = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

def jet(rock, gas):
    if gas == '>':
        move = 1
    else:
        move = -1
    return rock + [move, 0]

# List of rocks
rock0 = np.array([(0,0), (1,0), (2,0), (3,0)]) # -
rock1 = np.array([(1,0), (1,1), (0,1), (2,1), (1,2)]) # +
rock2 = np.array([(0,0), (1,0), (2,0), (2,1), (2,2)]) # mirrored L
rock3 = np.array([(0,0), (0,1), (0,2), (0,3)]) # |
rock4 = np.array([(0,0), (1,0), (0,1), (1,1)]) # cube
rocks = [rock0, rock1, rock2, rock3, rock4]

# Initiate parameters
height = 0
full_gases = gases*(2022//len(gases) + 1)
full_rocks = rocks*(2022//len(rocks) + 1)
settled_rocks = set()

# Iterate over rocks and gas jets
for n, rock in enumerate(full_rocks):
    # Set rock's initial position
    rock += [2, height + 3]
    for gas in full_gases: 
        # Jet of gas
        hashable_jet = set([tuple(i) for i in jet(rock, gas)])
        x_rock = list(zip(*hashable_jet))[0]
        x_max = max(x_rock)
        x_min = min(x_rock)
        if (x_min >= 0 and x_max <= 6) and\
           hashable_jet & settled_rocks == set():
            rock = jet(rock, gas)
       
        # Rock down
        
        hashable_rock = set([tuple(i) for i in (rock - 1)])
        if hashable_rock & settled_rocks != set() or\
            min(list(zip(*hashable_rock))[1]) == 0:
            settled_rocks.update(hashable_rock)
            height = max(list(zip(*rock))[1]) + 1
            break
        else:
            rock -= [0,1]
    if n == 2022:
        break

###### solve issues with velocity (probably related to search in set)
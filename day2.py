'''
Welcome to Advent of Code! 
Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2
'''

import argparse

parser = argparse.ArgumentParser(
    description = 'https://adventofcode.com/2022/day/2'
    )
parser.add_argument(
    'input', 
    type = str,
    help = 'Text file with each line containing two letters separated by a '\
        'space. The first one is either A, B or C and the second X, Y, Z.')
args = parser.parse_args()

def game_scenario(opponent:str, player:str) -> int:
    '''
    ### INPUT ###
    1) opponent = rock/paper/scissors from opponent
    2) player = rock/paper/scissors from player
    ### OUTPUT ###
    1) 0 if game lost, 3 if game tied, 6 if game won
    ### FUNCTION ###
    Given a rock-paper-scissors scenario, return the score
    '''
    # Tie
    if opponent == player:
        return 3
    # Winning
    elif (player == 'rock' and opponent == 'scissors') or\
        (player == 'scissors' and opponent == 'paper') or\
        (player == 'paper' and opponent == 'rock'):
        return 6
    # Losing
    else:
        return 0    

def rock_paper_scissors_1(input_url:str) -> int:
    '''
    ### INPUT ###
    1) input_url = input file url
    ### OUTPUT ###
    1) Rock-paper-scissors score
    ### FUNCTION ###
    Reads the input line by line, translates the letters to the score of a 
    rock-paper-scissors game and compute the final score.
    Disclaimer: the second column indicates the player's move
    '''
    letters_to_hand = {
        'A':'rock',
        'B':'paper',
        'C':'scissors',
        'X':'rock',
        'Y':'paper',
        'Z':'scissors'
        }
    hand_scores = {
        'rock':1,
        'paper':2,
        'scissors':3
        }
    with open(input_url) as game_file:
        score = 0
        for game_line in game_file.readlines():
            opponent, player =\
                [letters_to_hand[i]for i in game_line.rstrip('\n').split(' ')]
            score += hand_scores[player] + game_scenario(opponent, player)
    return score

def rock_paper_scissors_2(input_url:str) -> int:
    '''
    ### INPUT ###
    1) input_url = input file url
    ### OUTPUT ###
    1) Rock-paper-scissors score
    ### FUNCTION ###
    Reads the input file by line, translates the letters to the score of a 
    rock-paper-scissors game and compute the final score.
    Disclaimer: the second column indicates how the round has to end
    '''
    opponent_to_hand_score = {
        'A':[3,1,2],
        'B':[1,2,3],
        'C':[2,3,1],
        }
    outcome_to_points = {
        'X':0,
        'Y':3,
        'Z':6
        }
    
    with open(input_url) as game_file:
        score = 0
        for game_line in game_file.readlines():
            opponent, outcome = game_line.rstrip('\n').split(' ')
            opponent_index = list(outcome_to_points.keys()).index(outcome)
            score_based_on_opponent = opponent_to_hand_score[opponent][opponent_index]
            score += outcome_to_points[outcome] + score_based_on_opponent
    return score


def main():
    print(rock_paper_scissors_1(args.input))
    print(rock_paper_scissors_2(args.input))


if __name__ == "__main__":
    main()



"""
Author: Elaine Chan @elainechan01
Date: 12/2/22
Program: Advent of Calendar Day 2 - Rock Paper Scissors
"""

def main():
    # initialize scores
    move_score = {
        'A': 1,     # rock
        'B': 2,     # paper
        'C': 3      # scissors
    }
    translate_to_opp = {
        'X': 'A',   # rock
        'Y': 'B',   # paper
        'Z': 'C'    # scissors
    }
    # val: winning move 
    loss_pair = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }
    # val: losing move
    win_pair = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }
    f = open("d2-rock-paper-scissors/datasets/input.txt", "r")
    score = 0
    score_2 = 0
    try:
        # read lines and split by blank line
        f_contents = f.readlines()
        for item in f_contents:
            item = item.rstrip().split(' ')
            opp, me = item[0], item[1]
            # part 1
            # draw
            if opp == translate_to_opp[me]:
                score += 3
            # win
            elif loss_pair[opp] == translate_to_opp[me]:
                score += 6
            score += move_score[translate_to_opp[me]]
            # part 2
            # loss
            if me == 'X':
                score_2 += move_score[win_pair[opp]]
            # draw
            elif me == 'Y':
                score_2 += 3
                score_2 += move_score[opp]
            # win
            else:
                score_2 += 6
                score_2 += move_score[loss_pair[opp]]
        print(score)
        print(score_2)
    finally:
        f.close()

if __name__ == "__main__":
    main()
"""
Author: Elaine Chan @elainechan01
Date: 12/3/22
Program: Advent of Calendar Day 3 - Rucksack Reorganization
"""

import string
from collections import Counter

def main():
    score = 0
    score_2 = 0
    # initialize priority
    priority = {}
    i = 1
    for letter in string.ascii_lowercase:
        priority[letter] = i
        i += 1
    for letter in string.ascii_uppercase:
        priority[letter] = i
        i += 1
    f = open('d3-rucksack-reorg/datasets/input.txt', 'r')
    try:
        f_contents = f.readlines()
        three_elves = []
        for line in f_contents:
            line = line.strip()
            # split into two compartments
            mid = len(line)//2
            c1, c2 = line[0:mid], line[mid:]
            # get occurence counts
            c1_counter, c2_counter = Counter(c1), Counter(c2)
            # find cross matches
            match = [key for key in c1_counter.keys() if key in c2_counter.keys()]
            score += priority[match[0]] # assumption: there is only one match
            if len(three_elves) < 2:
                three_elves.append(line)
            else:
                three_elves.append(line)
                # get occurence counts of each three elves subgroup
                three_elves_counter = []
                for elf in three_elves:
                    three_elves_counter.append(Counter(elf))
                # find cross matches
                match = [key for key in three_elves_counter[0].keys() if key in three_elves_counter[1].keys() and key in three_elves_counter[2].keys()]
                score_2 += priority[match[0]] # assumption: there is only one match
                three_elves = []
    finally:
        f.close()
    print(score)
    print(score_2)


if __name__ == "__main__":
    main()
"""
Author: Elaine Chan @elainechan01
Date: 12/1/22
Program: Advent of Calendar Day 1 - Calorie Counting
"""

def main():
    f = open("d1-calorie-counting/datasets/input.txt", "r")
    try:
        # read lines and split by blank line
        f_contents = f.read()
        f_contents_split = f_contents.split('\n\n')
        # get total calories per elf
        elves = [sum([int(val) for val in item.split('\n')]) for item in f_contents_split]
        # sort by descending order
        desc_elves = sorted(elves,reverse=True)
        # part 1: find max val
        print(desc_elves[0])
        # part 2: find top three max val
        print(sum(desc_elves[0:3]))
    finally:
        f.close()

if __name__ == "__main__":
    main()
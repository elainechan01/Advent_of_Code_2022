"""
Author: Elaine Chan @elainechan01
Date: 12/9/22
Program: Advent of Calendar Day 6 - Tuning Trouble
"""

def main():
    f = open('d6-tuning-trouble/datasets/input.txt','r')
    try:
        # part 1: find start of packet marker (4 distinct characters)
        f_contents = f.readlines()
        f_contents = f_contents[0].rstrip()
        for i in range(len(f_contents)):
            window = [char for char in f_contents[i:i+4]]
            if sorted(window) == sorted(list(set(window))):
                print(i+4)
                break
        # part 2: find start of message market (14 distinct characters)
        for i in range(len(f_contents)):
            window = [char for char in f_contents[i:i+14]]
            if sorted(window) == sorted(list(set(window))):
                print(i+14)
                break
    finally:
        f.close()

if __name__ == "__main__":
    main()

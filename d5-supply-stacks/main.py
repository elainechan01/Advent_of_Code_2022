"""
Author: Elaine Chan @elainechan01
Date: 12/9/22
Program: Advent of Calendar Day 5 - Supply Stacks
"""

def initSupplyStacks() -> list:
    stacks = [[] for _ in range(9)]
    stacks[0] = ['Z','V','T','B','J','G','R']
    stacks[1] = ['L','V','R','J']
    stacks[2] = ['F','Q','S']
    stacks[3] = ['G','Q','V','F','L','N','H','Z']
    stacks[4] = ['W','M','S','C','J','T','Q','R']
    stacks[5] = ['F','H','C','T','W','S']
    stacks[6] = ['J','N','F','V','C','Z','D']
    stacks[7] = ['Q','F','R','W','D','Z','G','L']
    stacks[8] = ['P','V','W','B','J']
    return stacks

def main():
    stacks = initSupplyStacks()
    stacks2 = initSupplyStacks()
    f = open('d5-supply-stacks/datasets/input.txt', 'r')
    try:
        f_contents = f.readlines()
        for line in f_contents:
            # part 1: crates are popped from the top of a stack and added to the top of another stack until number of moves is reached
            # part 2: crates are popped from the top of a stack and added to the back of the newest add of another stack until number of moves is reached
            actions = line.rstrip().split(' ')
            for moves in range(int(actions[1])):
                # part 1
                stack = stacks[int(actions[3])-1].pop(0)
                stacks[int(actions[5])-1].insert(0, stack)
                # part 2
                stack2 = stacks2[int(actions[3])-1].pop(0)
                stacks2[int(actions[5])-1].insert(moves, stack2)
        print(''.join([stack[0] for stack in stacks]))
        print(''.join([stack[0] for stack in stacks2]))
    finally:
        f.close()

if __name__ == "__main__":
    main()

"""
Author: Elaine Chan @elainechan01
Date: 12/9/22
Program: Advent of Calendar Day 4 - Camp Cleanup
"""

def main():
    f = open('d4-camp-cleanup/datasets/input.txt', 'r')
    try:
        score = 0
        score_2 = 0
        f_contents = f.readlines()
        for line in f_contents:
            elves = line.rstrip('\n').split(',')
            # split line into [[elf 1 section 1, elf 1 section 2],[elf 2 section 1, elf 2 section 2]]
            elf_sections = [[int(section) for section in sections.split('-')] for sections in elves]
            # validate if one's elf's segments are completely enclosed within the other elf's
            if (elf_sections[0][0] >= elf_sections[1][0] and elf_sections[0][1] <= elf_sections[1][1]) or (elf_sections[0][0] <= elf_sections[1][0] and elf_sections[0][1] >= elf_sections[1][1]):
                score += 1
            # validate if there is an overlap at all
            if (elf_sections[0][0] <= elf_sections[1][1] and elf_sections[0][0] >= elf_sections[1][0]) or (elf_sections[1][0] <= elf_sections[0][1] and elf_sections[1][0] >= elf_sections[0][0]):
                score_2 += 1
        print(score)
        print(score_2)
    finally:
        f.close() 

if __name__ == "__main__":
    main()
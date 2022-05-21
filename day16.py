# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:37:14 2022

@author: mjenks
"""

def parse(puzzle_input):
    samples = []
    test = []
    i = 0
    while i < len(puzzle_input):
        line = puzzle_input[i].strip().split()
        if len(line) == 0:
            i += 1
        elif line[0] == 'Before:':
            sample = [(int(line[1][1:-1]),int(line[2][:-1]),int(line[3][:-1]),int(line[4][:-1]))]
            i += 1
            line = puzzle_input[i].strip().split()
            sample.append(tuple([int(x) for x in line]))
            i += 1
            line = puzzle_input[i].strip().split()
            sample.append((int(line[1][1:-1]),int(line[2][:-1]),int(line[3][:-1]),int(line[4][:-1])))
            samples.append(sample)
            i += 1
        else:
            test.append([int(x) for x in line])
            i += 1
    return samples, test
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day16.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
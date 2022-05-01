# -*- coding: utf-8 -*-
"""
Created on Sun May 01 15:21:10 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        month = int(line[0][-5:-3])
        day = int(line[0][-2:])
        minute = int(line[1][3:-1])
        action = line[2]
        if action == 'Guard':
            num = int(line[3][1:])
            data.append([(month, day), minute, num])
        else:
            data.append([(month, day), minute, action])
    data.sort()
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day4.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
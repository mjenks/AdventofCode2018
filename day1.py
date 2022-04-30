# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:44:49 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = list(line.strip())
        sign = line[0]
        value = int(''.join(line[1:]))
        if sign == '+':
            data.append(value)
        else:
            data.append(-1*value)
    return data
    
def solve(puzzle_data):
    return sum(puzzle_data), 0

puzzle_path = "input_day1.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
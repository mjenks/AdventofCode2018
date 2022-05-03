# -*- coding: utf-8 -*-
"""
Created on Tue May 03 18:03:19 2022

@author: mjenks
"""

import string

def parse(puzzle_input):
    data = [[] for x in range(26)]
    for line in puzzle_input:
        line = line.strip().split()
        step = line[7]
        req = line[1]
        data[string.uppercase.index(step)].append(req)
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day7.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
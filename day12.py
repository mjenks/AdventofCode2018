# -*- coding: utf-8 -*-
"""
Created on Sun May 08 22:16:38 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = {}
    line = puzzle_input[0]
    start = line.strip().split(': ')[1]
    for line in puzzle_input[2:]:
        rule = line.strip().split(' => ')
        data[rule[0]] = rule[1]
    return start, data    
    
def solve(puzzle_data):
    initial, rules = puzzle_data
    return 0, 0

puzzle_path = "input_day12.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
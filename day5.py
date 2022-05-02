# -*- coding: utf-8 -*-
"""
Created on Mon May 02 11:02:02 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = [ord(x) for x in puzzle_input.strip()]
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day5.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
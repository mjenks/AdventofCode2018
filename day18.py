# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 12:13:14 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day18.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
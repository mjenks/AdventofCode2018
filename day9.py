# -*- coding: utf-8 -*-
"""
Created on Thu May 05 21:47:22 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = puzzle_input.strip().split()
    return int(data[0]), int(data[6])
    
def solve(puzzle_data):
    num_players, last_marble = puzzle_data
    return 0, 0

puzzle_path = "input_day9.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
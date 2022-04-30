# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:03:35 2022

@author: mjenks
"""

from collections import Counter

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip()
        data.append(line)
    return data
    
def solve(puzzle_data):
    double = 0
    triple = 0
    for box in puzzle_data:
        counts = Counter(box)
        if 2 in counts.values():
            double += 1
        if 3 in counts.values():
            triple += 1
    return double*triple, 0

puzzle_path = "input_day2.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
# -*- coding: utf-8 -*-
"""
Created on Mon May 02 11:02:02 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = [ord(x) for x in puzzle_input.strip()]
    return data
    
def solve(puzzle_data):
    length = 0
    polymer = puzzle_data[:]
    while length != len(polymer):
        length = len(polymer)
        new = []
        i = 0
        while i < length:
            if i == length - 1:
                new.append(polymer[i])
                i += 1
            elif polymer[i] - 32 == polymer[i+1] or polymer[i] + 32 == polymer[i+1]:
                i += 2
            else:
                new.append(polymer[i])
                i += 1
        polymer = new[:]
    
    return length, 0

puzzle_path = "input_day5.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
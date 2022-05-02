# -*- coding: utf-8 -*-
"""
Created on Mon May 02 11:02:02 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = [ord(x) for x in puzzle_input.strip()]
    return data
    
def shrink(polymer):
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
    return new[:]
    
def shrink_len(polymer):
    length = 0
    while length != len(polymer):
        length = len(polymer)
        polymer = shrink(polymer)
    return length
    
def solve(puzzle_data):
    poly_len = []
    for val in range(65,91):
        polymer = [x for x in puzzle_data if (x != val) and (x != val+32)]
        poly_len.append(shrink_len(polymer))
    return shrink_len(puzzle_data), min(poly_len)

puzzle_path = "input_day5.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
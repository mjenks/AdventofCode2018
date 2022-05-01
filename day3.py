# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:29:13 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip()
        elf = line.split()[0]
        line = line.split(': ')
        y = int(line[0].split(',')[0].split()[-1])
        x = int(line[0].split(',')[1])
        w = int(line[1].split('x')[0])
        h = int(line[1].split('x')[0])
        data.append([elf,y,x,w,h])
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day3.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
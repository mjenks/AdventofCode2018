# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:29:13 2022

@author: mjenks
"""

import numpy as np

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip()
        elf = line.split()[0]
        line = line.split(': ')
        x = int(line[0].split(',')[0].split()[-1])
        y = int(line[0].split(',')[1])
        w = int(line[1].split('x')[0])
        h = int(line[1].split('x')[1])
        data.append([elf,x,y,w,h])
    return data
    
def solve(puzzle_data):
    size = 1000
    cloth = np.zeros((size,size))
    
    for elf in puzzle_data:
        ident, x, y, w, h = elf
        cloth[x:x+w, y:y+h] += 1
    for elf in puzzle_data:
        ident, x, y, w, h = elf
        if np.all(cloth[x:x+w, y:y+h] == 1):
            intact = ident
    overlap = np.size(np.where(cloth >= 2)[0])
    return overlap, intact[1:]

puzzle_path = "input_day3.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
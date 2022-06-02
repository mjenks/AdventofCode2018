# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 14:43:15 2022

@author: rikku
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split(',')
        direction = line[0][0]
        val = int(line[0].split('=')[1])
        ran = [int(x) for x in line[1].split('=')[1].split('..')]
        data.append((direction,val,ran))
    return data

def mapclay(grid,data):
    for vein in data:
        if vein[0] == 'x':
            ran = vein[2]
            for j in range(ran[0],ran[1]+1):
                grid[j][vein[1]] = '#'
        else:
            ran = vein[2]
            for i in range(ran[0],ran[1]+1):
                grid[vein[1]][i] = '#'                
    return grid
    
def solve(puzzle_data):
    grid = [['.' for i in range(700)] for j in range(2000)]
    #add spring
    grid[0][500] = '+'
    grid = mapclay(grid,puzzle_data)
    return 0, 0

puzzle_path = "input_day17.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
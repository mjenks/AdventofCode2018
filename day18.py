# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 12:13:14 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip()
        data.append(list(line))
    return data

def morph(grid):
    new_grid = []
    for j in range(50):
        new_row = []
        for i in range(50):
            adjecent = []
            if j != 0:
                if i != 0:
                    adjecent.append(grid[j-1][i-1])
                adjecent.append(grid[j-1][i])
                if i != 49:
                    adjecent.append(grid[j-1][i+1])
            if j != 49:
                if i != 0:
                    adjecent.append(grid[j+1][i-1])
                adjecent.append(grid[j+1][i])
                if i != 49:
                    adjecent.append(grid[j+1][i+1])
            if i != 0:
                adjecent.append(grid[j][i-1])
            if i != 49:
                adjecent.append(grid[j][i+1])
            cur = grid[j][i]
            if cur == '.':
                if sum([1 for x in adjecent if x == '|']) >= 3:
                    new_row.append('|')
                else:
                    new_row.append(cur)
            elif cur == '|':
                if sum([1 for x in adjecent if x == '#']) >= 3:
                    new_row.append('#')
                else:
                    new_row.append(cur)
            else:
                if '|' in adjecent and '#' in adjecent:
                    new_row.append(cur)
                else:
                    new_row.append('.')
        new_grid.append(new_row)
    return new_grid    
    
def solve(puzzle_data):
    grid = puzzle_data
    time = 0
    while time < 10:
        grid = morph(grid)
        time += 1
    wooded = sum([sum([1 for x in row if x == '|']) for row in grid])
    lumber = sum([sum([1 for x in row if x == '#']) for row in grid])
    return wooded*lumber, 0

puzzle_path = "input_day18.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
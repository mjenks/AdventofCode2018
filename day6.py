# -*- coding: utf-8 -*-
"""
Created on Mon May 02 12:54:06 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append([int(x) for x in line.strip().split(', ')])
    return data
    
def closest(x,y,points):
    dist = [abs(x-i) + abs(y-j) for i, j in points]
    close = min(dist)
    if dist.count(close) == 1:
        return dist.index(close)
    else:
        return -1
    
def solve(puzzle_data):
    grid = [['.' for i in range(400)] for j in range(400)]
    for y in range(400):
        for x in range(400):
            grid[y][x] = closest(x,y, puzzle_data)
    inf = [False for i in puzzle_data]
    edge = set(grid[0]) | set(grid[-1]) | set([a[0] for a in grid]) | set([a[-1] for a in grid])
    for val in edge:
        inf[val] = True
    size = []
    largest_area = 0
    for i in range(len(puzzle_data)):
        size.append(sum([a.count(i) for a in grid]))
        if not inf[i]:
            largest_area = max(largest_area, size[i])
    return largest_area, 0

puzzle_path = "input_day6.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
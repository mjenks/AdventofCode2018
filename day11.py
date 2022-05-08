# -*- coding: utf-8 -*-
"""
Created on Sat May 07 21:30:32 2022

@author: mjenks
"""

def power(x, y, num):
    rack_id = x + 10
    pl = str(((rack_id*y) + num)*rack_id)
    if len(pl) >= 3:
        power_level = int(pl[-3])
    else:
        power_level = 0
    return power_level - 5
    
def max_square(grid, size):
    max_power = 0
    corner = (0,0)
    for y in range(300-size):
        for x in range(300-size):
            tot_power = sum([sum(a[x:x+size]) for a in grid[y:y+size]])
            if tot_power > max_power:
                max_power = tot_power
                corner = (x+1, y+1)
    return max_power, corner
    
def solve(puzzle_data):
    grid = [[power(i, j, puzzle_data) for i in range(1,301)] for j in range(1,301)]
    boxes = []
    i = 3
    sqr = max_square(grid, 3) 
    boxes.append(sqr)
    while sqr[0] > 0:
        i += 1
        sqr = max_square(grid, i)
        boxes.append(sqr)
    size = 3 + boxes.index(max(boxes))
    corner = max(boxes)[1]
    return boxes[0][1], (corner, size)
    
puzzle_data = 7803
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
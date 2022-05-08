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
    
def solve(puzzle_data):
    grid = [[power(i, j, puzzle_data) for i in range(1,301)] for j in range(1,301)]
    max_power = 0
    for y in range(297):
        for x in range(297):
            tot_power = sum([sum(a[x:x+3]) for a in grid[y:y+3]])
            if tot_power > max_power:
                max_power = tot_power
                corner = (x+1, y+1)
        
    return corner, 0

    
puzzle_data = 7803
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
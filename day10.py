# -*- coding: utf-8 -*-
"""
Created on Fri May 06 15:37:17 2022

@author: mjenks
"""

class Point():
    def __init__(self, position, velocity):
        self.x, self.y = position
        self.vx, self.vy = velocity

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split('=')
        pos = line[1][1:-10]
        vel = line[2][1:-1]
        pos = [int(a) for a in pos.split(',')]
        vel = [int(a) for a in vel.split(',')]
        data.append(Point(pos,vel))
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day10.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
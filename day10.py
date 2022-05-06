# -*- coding: utf-8 -*-
"""
Created on Fri May 06 15:37:17 2022

@author: mjenks
"""

class Point():
    def __init__(self, position, velocity):
        self.x, self.y = position
        self.vx, self.vy = velocity
    def move(self, step = 1):
        self.x += self.vx *step
        self.y += self.vy *step

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
    t = 10080
    for p in puzzle_data:
        p.move(10080)
    while t < 10090:
        t += 1
        for p in puzzle_data:
            p.move(1)
        x_max = max([a.x for a in puzzle_data])
        x_min = min([a.x for a in puzzle_data])
        y_max = max([a.y for a in puzzle_data])
        y_min = min([a.y for a in puzzle_data])
        if y_max - y_min < 12:
            grid = [['.' for i in range(x_max - x_min + 1)] for j in range(y_max - y_min + 1)]
            for pt in puzzle_data:
                grid[pt.y-y_min][pt.x-x_min] = '#'
            print(t)
            for row in grid:
                print(''.join(row))

    return 0, 0

puzzle_path = "input_day10.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
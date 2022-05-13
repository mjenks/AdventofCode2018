# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:41:20 2022

@author: mjenks
"""

class Unit:
    def __init__(self, x, y):
        self.hp = 200
        self.attack = 3
        self.x = x
        self.y = y

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(list(line.strip()))
    goblins = []
    elves = []
    for j in range(len(data)):
        for i in range(len(data[0])):
            if data[j][i] == 'G':
                goblins.append(Unit(i,j))
            elif data[j][i] == 'E':
                elves.append(Unit(i,j))
    return data, goblins, elves
    
def solve(puzzle_data):
    grid, goblins, elves = puzzle_data

    return 0, 0

puzzle_path = "input_day15.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
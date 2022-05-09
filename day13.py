# -*- coding: utf-8 -*-
"""
Created on Mon May 09 13:37:35 2022

@author: mjenks
"""

class Cart():
    turns = ['l', 's', 'r']
    def __init__(self, x, y, facing):
        self.turn_index = 0
        self.x = x
        self.y = y
        self.facing = facing

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line[:-1]
        data.append(list(line))
    carts = []
    for j in range(len(data)):
        for i in range(len(data[0])):
            if data[j][i] == '<':
                carts.append(Cart(i, j, 'l'))
                data[j][i] = '-'
            elif data[j][i] == '>':
                carts.append(Cart(i, j, 'r'))
                data[j][i] = '-'
            elif data[j][i] == 'v':
                carts.append(Cart(i, j, 'd'))
                data[j][i] = '|'
            elif data[j][i] == '^':
                carts.append(Cart(i, j, 'u'))
                data[j][i] = '|'
                
    return data, carts
    
def solve(puzzle_data):
    track, carts = puzzle_data
    return 0, 0

puzzle_path = "input_day13.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
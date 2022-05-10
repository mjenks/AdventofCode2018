# -*- coding: utf-8 -*-
"""
Created on Mon May 09 13:37:35 2022

@author: mjenks
"""

import collections

class Cart():
    turns = ['l', 's', 'r']
#    compass = ['u', 'r', 'd', 'l']
    def __init__(self, x, y, facing):
        self.turn_index = 0
        self.x = x
        self.y = y
        self.facing = facing
    def move(self):
        if self.facing == 3:
            self.x -= 1
        elif self.facing == 0:
            self.y -= 1
        elif self.facing == 1:
            self.x += 1
        elif self.facing == 2:
            self.y += 1
    def turn(self):
        trn = self.turns[self.turn_index]
        self.turn_index = (self.turn_index + 1)%3
        if trn == 'l':
            self.facing -= 1
        elif trn == 'r':
            self.facing += 1
        self.facing = self.facing%4

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line[:-1]
        data.append(list(line))
    carts = []
    for j in range(len(data)):
        for i in range(len(data[0])):
            if data[j][i] == '<':
                carts.append(Cart(i, j, 3))
                data[j][i] = '-'
            elif data[j][i] == '>':
                carts.append(Cart(i, j, 1))
                data[j][i] = '-'
            elif data[j][i] == 'v':
                carts.append(Cart(i, j, 2))
                data[j][i] = '|'
            elif data[j][i] == '^':
                carts.append(Cart(i, j, 0))
                data[j][i] = '|'
                
    return data, carts
    
def solve(puzzle_data):
    track, carts = puzzle_data
    ticks = 0
    collision = False
    while not collision:
        for cart in carts:
            cart.move()
            if track[cart.y][cart.x] == '/':
                if cart.facing%2 == 0:
                    cart.facing = (cart.facing + 1)%4
                else:
                    cart.facing = (cart.facing - 1)%4
            if track[cart.y][cart.x] == '\\':
                if cart.facing%2 == 0:
                    cart.facing = (cart.facing - 1)%4
                else:
                    cart.facing = (cart.facing + 1)%4
            elif track[cart.y][cart.x] == '+':
                cart.turn()
        ticks += 1
        locations = [(c.x, c.y) for c in carts]
        if len(locations) != len(set(locations)):
            collision = True
    collision_points = [a for a, b in collections.Counter(locations).items() if b > 1]
    return collision_points, 0

puzzle_path = "input_day13.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
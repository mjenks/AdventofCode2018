# -*- coding: utf-8 -*-
"""
Created on Thu May 05 21:47:22 2022

@author: mjenks
"""

from collections import deque

def parse(puzzle_input):
    data = puzzle_input.strip().split()
    return int(data[0]), int(data[6])
    
def solve(puzzle_data):
    num_players, last_marble = puzzle_data
    circle = deque([0])
    scores = [0 for i in range(num_players)]
    elf = 0
    for marble in range(1,last_marble+1):
        if marble%23 == 0:
            circle.rotate(7)
            scores[elf] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
        elf = (elf+1)%num_players
    return max(scores)

puzzle_path = "input_day9.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
print "tests:"
print solve((9,25)), 32
#10 players; last marble is worth 1618 points: high score is 8317
print solve((10,1618)), 8317
#13 players; last marble is worth 7999 points: high score is 146373
print solve((13,7999)), 146373
#17 players; last marble is worth 1104 points: high score is 2764
print solve((17,1104)), 2764
#21 players; last marble is worth 6111 points: high score is 54718
print solve((21,6111)), 54718
#30 players; last marble is worth 5807 points: high score is 37305  
print solve((30,5807)), 37305
    
puzzle_data = parse(puzzle_input)
solution1 = solve(puzzle_data)
puzzle_data = list(puzzle_data)
puzzle_data[1] = puzzle_data[1]*100
solution2 = solve(puzzle_data)

print "Solutions:"
print(solution1)
print(solution2)
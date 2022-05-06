# -*- coding: utf-8 -*-
"""
Created on Thu May 05 21:47:22 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = puzzle_input.strip().split()
    return int(data[0]), int(data[6])
    
def solve(puzzle_data):
    num_players, last_marble = puzzle_data
    circle = [0]
    current = 0
    scores = [0 for i in range(num_players)]
    elf = 0
    for marble in range(1,last_marble+1):
        if marble%23 == 0:
            bonus = (current - 7)%len(circle)
            scores[elf] += marble + circle[bonus]
            del circle[bonus]
            current = bonus%len(circle)
        else:
            current = (current + 2)%len(circle)
            if current == 0:
                circle.insert(len(circle), marble)
                current = len(circle) - 1
            else:
                circle.insert(current, marble)
        elf = (elf+1)%num_players
    
    return max(scores), scores.index(max(scores))

puzzle_path = "input_day9.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
print "tests:"
print solve((9,25))[0], 32
#10 players; last marble is worth 1618 points: high score is 8317
print solve((10,1618))[0], 8317
#13 players; last marble is worth 7999 points: high score is 146373
print solve((13,7999))[0], 146373
#17 players; last marble is worth 1104 points: high score is 2764
print solve((17,1104))[0], 2764
#21 players; last marble is worth 6111 points: high score is 54718
print solve((21,6111))[0], 54718
#30 players; last marble is worth 5807 points: high score is 37305  
print solve((30,5807))[0], 37305
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print "Solutions:"
print(solution1)
print(solution2)
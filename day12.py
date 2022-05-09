# -*- coding: utf-8 -*-
"""
Created on Sun May 08 22:16:38 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = {}
    line = puzzle_input[0]
    start = line.strip().split(': ')[1]
    for line in puzzle_input[2:]:
        rule = line.strip().split(' => ')
        data[rule[0]] = rule[1]
    return start, data    
    
def next_gen(pots):
    new = []
    for i in range(-2, len(pots)+2):
        if i == -2:
            area = ['.','.','.','.',pots[i+2]]
        elif i == -1:
            area = ['.','.','.']
            area.append(pots[i+1])
            area.append(pots[i+2])
        elif i == 0:
            area = ['.','.']
            area.append(pots[i])
            area.append(pots[i+1])
            area.append(pots[i+2])
        elif i == 1:
            area = ['.']
            area.append(pots[i-1])
            area.append(pots[i])
            area.append(pots[i+1])
            area.append(pots[i+2])
        elif i == len(pots)-2:
            area = pots[i-2:]
            area.append('.')
        elif i == len(pots) -1:
            area = pots[i-2:]
            area.append('.')
            area.append('.')
        elif i == len(pots):
            area = pots[i-2:]
            area.append('.')
            area.append('.')
            area.append('.')
        elif i == len(pots) + 1:
            area = [pots[-1], '.','.','.','.']
        else:
            area = pots[i-2:i+3]
        new.append(rules[''.join(area)])
    return new
    
def solve(puzzle_data):
    pots = list(puzzle_data)
    first_pot = 0
    for gen in range(20):
        pots = next_gen(pots)
        first_pot -= 2
    return sum([i + first_pot for i in range(len(pots)) if pots[i] == '#']), 0

puzzle_path = "input_day12.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data, rules = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
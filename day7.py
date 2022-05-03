# -*- coding: utf-8 -*-
"""
Created on Tue May 03 18:03:19 2022

@author: mjenks
"""

import string

def parse(puzzle_input):
    data = [[] for x in range(26)]
    for line in puzzle_input:
        line = line.strip().split()
        step = line[7]
        req = line[1]
        data[string.uppercase.index(step)].append(req)
    return data
    
def solve(puzzle_data):
    complete = [False for x in puzzle_data]
    avail = set()
    order = []
    while False in complete:
        for step in range(len(puzzle_data)):
            needed = puzzle_data[step]
            met = True
            for req in needed:
                if not complete[string.uppercase.index(req)]:
                    met = False
            if met and not complete[step]:
                avail.add(step)
        task = min(avail)
        complete[task] = True
        avail.remove(task)
        order.append(task)
    return ''.join([string.uppercase[step] for step in order]), 0

puzzle_path = "input_day7.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
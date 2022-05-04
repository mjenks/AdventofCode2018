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
    
def solve1(puzzle_data):
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
    return ''.join([string.uppercase[step] for step in order])
    
def solve2(puzzle_data):
    working = 0
    time = 0
    complete = [False for x in puzzle_data]
    pending = [-1 for x in puzzle_data]
    avail = set()
    while False in complete:
        for step in range(len(puzzle_data)):
            if pending[step] == time:
                working -= 1
                complete[step] = True
        for step in range(len(puzzle_data)):
            needed = puzzle_data[step]
            met = True
            for req in needed:
                if not complete[string.uppercase.index(req)]:
                    met = False
            if met and not complete[step] and pending[step] == -1:
                avail.add(step)
        while working <= 5 and len(avail) > 0:
            task = min(avail)
            working += 1
            pending[task] = time + 61 + task
            avail.remove(task)
        time += 1
    return time -1

puzzle_path = "input_day7.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = solve1(puzzle_data)
solution2 = solve2(puzzle_data)

print(solution1)
print(solution2)
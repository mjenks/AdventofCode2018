# -*- coding: utf-8 -*-
"""
Created on Sun May 01 15:21:10 2022

@author: mjenks
"""

guard = {}

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        month = int(line[0][-5:-3])
        day = int(line[0][-2:])
        minute = int(line[1][3:-1])
        action = line[2]
        if line[1][:2] == '23':
            minute -= 60
            day += 1
        if action == 'Guard':
            num = int(line[3][1:])
            data.append([(month, day), minute, num])
            guard[num] = []
        else:
            data.append([(month, day), minute, action])
    data.sort()
    return data
    
def solve(puzzle_data):
    duty = 0
    start = 0
    asleep = {}
    hour = {}
    for g in guard.keys():
        asleep[g] = 0
        hour[g] = [0 for i in range(60)]
    for i in range(len(puzzle_data)):
        log = puzzle_data[i]
        minute = log[1]
        if type(log[2]) == int:
            duty = log[2]
        elif log[2] == 'falls':
            start = minute
        elif log[2] == 'wakes':
            if start > minute:
                print log, start
            guard[duty].append((start,minute))
            asleep[duty] += minute - start
    guard_chosen = asleep.keys()[asleep.values().index(max(asleep.values()))]
    freq_sleep = []
    for gd in guard.keys():
        for sleep in guard[gd]:
            start, end = sleep
            for t in range(start,end):
                hour[gd][t] += 1
        freq_sleep.append((gd, max(hour[gd])))
    min_chosen = hour[guard_chosen].index(max(hour[guard_chosen]))
    guard2, freq = max(freq_sleep, key = lambda x:x[1])
    min2 = hour[guard2].index(freq)
    return guard_chosen*min_chosen, guard2*min2

puzzle_path = "input_day4.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
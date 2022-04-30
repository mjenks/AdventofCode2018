# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:29:13 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip()
        elf = line.split()[0]
        line = line.split(': ')
        x = int(line[0].split(',')[0].split()[-1])
        y = int(line[0].split(',')[1])
        w = int(line[1].split('x')[0])
        h = int(line[1].split('x')[0])
        data.append([elf,x,y,w,h])
    return data
    
def solve(puzzle_data):
    cloth = [['.' for j in range(1100)] for i in range(1100)]
    overlap = 0
    for elf in puzzle_data:
        y = elf[1]
        x = elf[2]
        w = elf[3]
        h = elf[4]
        for a in range(y,y+h):
            for b in range(x,x+w):
                if cloth[a][b] == '.':
                    cloth[a][b] = elf[0]
                else:
                    cloth[a][b] = 'x'
    for row in cloth:
        overlap += row.count('x')
    return overlap, cloth

puzzle_path = "input_day3.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
#print(solution2)
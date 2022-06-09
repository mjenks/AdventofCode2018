# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 10:45:31 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        if line[0] == '#ip':
            point = int(line[-1])
        else:
            com = line[0]
            a = line[1]
            b = line[2]
            c = int(line[3])
            inst = com + "(reg," + a + ',' + b + ')'
            data.append([inst,c])
    return point, data
    
def addr(reg,a,b):
    return reg[a]+reg[b]

def addi(reg,a,b):
    return reg[a]+b

def mulr(reg,a,b):
    return reg[a]*reg[b]

def muli(reg,a,b):
    return reg[a]*b

def banr(reg,a,b):
    return reg[a]&reg[b]
    
def bani(reg,a,b):
    return reg[a]&b
    
def borr(reg,a,b):
    return reg[a] | reg[b]
    
def bori(reg,a,b):
    return reg[a] | b
    
def setr(reg,a,b):
    return reg[a]
    
def seti(reg,a,b):
    return a
    
def gtir(reg,a,b):
    if a > reg[b]:
        return 1
    else:
        return 0
        
def gtri(reg,a,b):
    if reg[a] > b:
        return 1
    else:
        return 0
        
def gtrr(reg,a,b):
    if reg[a] > reg[b]:
        return 1
    else:
        return 0
        
def eqir(reg,a,b):
    if a == reg[b]:
        return 1
    else:
        return 0

def eqri(reg,a,b):
    if reg[a] == b:
        return 1
    else:
        return 0

def eqrr(reg,a,b):
    if reg[a] == reg[b]:
        return 1
    else:
        return 0  
    
def solve(puzzle_data):
    reg = [0,0,0,0,0,0]
    point, code = puzzle_data
    i = 0
    while i >= 0 and i < len(code):
        reg[point] = i
        inst = code[i]
        reg[inst[1]] = eval(inst[0])
        i = reg[point]
        i += 1
    return reg[0], 0

puzzle_path = "input_day19.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
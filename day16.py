# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:37:14 2022

@author: mjenks
"""

codes = {0:set(),
         1:set(),
         2:set(),
         3:set(),
         4:set(),
         5:set(),
         6:set(),
         7:set(),
         8:set(),
         9:set(),
         10:set(),
         11:set(),
         12:set(),
         13:set(),
         14:set(),
         15:set()}

def parse(puzzle_input):
    samples = []
    test = []
    i = 0
    while i < len(puzzle_input):
        line = puzzle_input[i].strip().split()
        if len(line) == 0:
            i += 1
        elif line[0] == 'Before:':
            sample = [(int(line[1][1:-1]),int(line[2][:-1]),int(line[3][:-1]),int(line[4][:-1]))]
            i += 1
            line = puzzle_input[i].strip().split()
            sample.append(tuple([int(x) for x in line]))
            i += 1
            line = puzzle_input[i].strip().split()
            sample.append((int(line[1][1:-1]),int(line[2][:-1]),int(line[3][:-1]),int(line[4][:-1])))
            samples.append(sample)
            i += 1
        else:
            test.append([int(x) for x in line])
            i += 1
    return samples, test
    
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
        
def testSample(sample):
    before, code, after = sample
    reg = before
    num = code[0]
    a = code[1]
    b = code[2]
    c = code[3]
    match = 0
    opcodes = [addr,addi,mulr,muli,bani,banr,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]
    for op in opcodes:
        if op(reg,a,b) == after[c]:
            codes[num].add(op)
            match += 1
    return match >= 3
    
def solve(puzzle_data):
    samples, test = puzzle_data
    count = sum([testSample(s) for s in samples])
    found = [3] #start with 3 because it only has one option
    #finds the number code for each opcode
    for x in found:
        for code in codes:
            if code == x:
                continue
            if len(codes[code]) == 1:
                continue
            else:
                codes[code] = codes[code] - codes[x]
                if len(codes[code]) == 1:
                    found.append(code)
    #make codes a dictionary of functions rather than sets of functions
    for code in codes:
        codes[code] = next(iter(codes[code]))
    reg = [0,0,0,0]
    for line in test:
        reg[line[3]] = codes[line[0]](reg,line[1],line[2])
    return count, reg[0]

puzzle_path = "input_day16.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 14:43:15 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split(',')
        direction = line[0][0]
        val = int(line[0].split('=')[1])
        ran = [int(x) for x in line[1].split('=')[1].split('..')]
        data.append((direction,val,ran))
    return data

def mapclay(grid,data):
    for vein in data:
        if vein[0] == 'x':
            ran = vein[2]
            for j in range(ran[0],ran[1]+1):
                grid[j][vein[1]] = '#'
        else:
            ran = vein[2]
            for i in range(ran[0],ran[1]+1):
                grid[vein[1]][i] = '#'                
    return grid

def fillrow(grid, x, y):
    #look for walls on each side of y row
    r = grid[y][x:]
    l = grid[y][:x]
    l.reverse()
    try:
        rw = r.index('#') + len(l)
        lw = len(l) - l.index('#') - 1
        for i in range(lw+1,rw):
            if grid[y+1][i] == '.':
                walled = False
                return grid, walled
        for i in range(lw+1,rw):
            grid[y][i] = '~'
        walled = True
    except:
        walled = False
    return grid, walled
    
def overflow(grid, x, y):
    fall = []
    if grid[y][x] == '.':
        grid[y][x] = '|'
    #overflow to left
    end = False
    i = x
    while not end:
        i -= 1
        if grid[y][i] == '#': #hit wall
            end = True
        elif grid[y+1][i] == '.' or grid[y+1][i] == '|':
            end = True
            fall.append(i)
            grid[y][i] = '|'
        else:
            grid[y][i] = '|'      
    #overflow to right
    end = False
    i = x
    while not end:
        i += 1
        if grid[y][i] == '#': #hit wall
            end = True
        elif grid[y+1][i] == '.' or grid[y+1][i] == '|':
            end = True
            fall.append(i)
            grid[y][i] = '|'
        else:
            grid[y][i] = '|'  
    return grid, fall
    
def fill(grid, x, y):
    walled = True
    i = 0
    while walled:
        i += 1
        grid, walled = fillrow(grid,x,y-i)
    grid, fall = overflow(grid, x, y-i)
    for drop in fall:
        for j in range(y-i,y):
            if grid[j+1][drop] == '.':
                grid[j+1][drop] = '|'
            elif grid[j+1][drop] == '#' or grid[j+1][drop] == '~':
                grid = fill(grid,drop,j+1)
    return grid
    
def solve(puzzle_data):
    grid = [['.' for i in range(700)] for j in range(2000)]
    #add spring
    grid[0][500] = '+'
    grid = mapclay(grid,puzzle_data)
    hasclay = ['#' in row for row in grid]
    y_min = hasclay.index(True)
    hasclay.reverse()
    y_max = len(hasclay) - hasclay.index(True)
    prior = grid[0]
    for j in range(1,len(grid)):
        row = grid[j]
        for i in range(len(row)):
            if prior[i] == '|' or prior[i] == '+':
                if row[i] == '#':
                    grid = fill(grid, i, j)
                elif row[i] == '.':
                    grid[j][i] = '|'
        prior = row
    filled = sum([sum([x == '~' for x in row]) for row in grid[y_min:y_max]])
    touched = sum([sum([x == '|' for x in row]) for row in grid[y_min:y_max]])
    return filled+touched, filled

puzzle_path = "input_day17.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
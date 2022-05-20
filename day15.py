# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:41:20 2022

@author: mjenks
"""

class Unit:
    def __init__(self, race, x, y):
        self.race = race
        self.hp = 200
        self.attack = 3
        self.x = x
        self.y = y

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(list(line.strip()))
    units = []
    for j in range(len(data)):
        for i in range(len(data[0])):
            if data[j][i] == 'G':
                units.append(Unit('G',i,j))
            elif data[j][i] == 'E':
                units.append(Unit('E',i,j))
    return data, units
    
def inrange(enemies):
    global grid
    avail = []
    for enemy in enemies:
        i = enemy.x
        j = enemy.y
        if i > 0:
            point = grid[j][i-1]
            if point == '.':
                avail.append((i-1,j))
        if i < len(grid[0]):
            point = grid[j][i+1]
            if point == '.':
                avail.append((i+1,j))
        if j > 0:
            point = grid[j-1][i]
            if point == '.':
                avail.append((i,j-1))
        if j < len(grid):
            point = grid[j+1][i]
            if point == '.':
                avail.append((i,j+1))
    return avail
    
def isopen(x,y):
    global grid
    if grid[y][x] == '.':
        return True
    else:
        return False
    
def step(current, visited):
    options = []
    for point in current:
        x, y = point
        if isopen(x+1,y) and (x+1,y) not in visited:
            spot = x+1, y
            visited.add(spot)
            options.append(spot)
        if isopen(x,y+1) and (x,y+1) not in visited:
            spot = x, y+1
            visited.add(spot)
            options.append(spot)
        if isopen(x-1, y) and (x-1,y) not in visited:
            spot = x-1, y
            visited.add(spot)
            options.append(spot)
        if isopen(x, y-1) and (x,y-1) not in visited:
            spot = x, y-1
            visited.add(spot)
            options.append(spot)
    return options, visited    
    
def findNearest(unit, points):
    location = [(unit.x,unit.y)]
    steps = 0
    shortest_routes = [0 for a in range(len(points))]
    visited = set()
    visited.add(location[0])
    nearest = []
    while sum(shortest_routes) == 0 and len(location) > 0 and steps < 1000: #1000 covers traversing the whole grid
        steps += 1
        location, visited = step(location, visited)
        for spot in location:
            if spot in points:
                index = points.index(spot)
                if shortest_routes[index] == 0:
                    shortest_routes[index] = steps
                    nearest.append(spot)
    if len(nearest) == 0: #no path to points exists
        return (unit.x, unit.y)
    else:
        nearest.sort(key=lambda p: (p[1], p[0]))
        return nearest[0]
    
def findPath(unit, des):
    location = [des]
    steps = 0
    visited = set()
    visited.add(location[0])
    points = [(unit.x,unit.y-1),(unit.x-1,unit.y),(unit.x+1,unit.y),(unit.x,unit.y+1)]
    found = False
    choice = []
    while not found:
        steps += 1
        for spot in location:
            if spot in points:
                choice.append(spot)
                found = True
        location, visited = step(location, visited)
    choice.sort(key=lambda p: (p[1],p[0])) #sort to reading order
    return choice[0] 
    
def move(unit, enemies):
    global grid
    enemies = [e for e in enemies if e.hp > 0]
    e_loc = set([(e.x,e.y) for e in enemies])
    adj = set([(unit.x+1,unit.y),(unit.x-1,unit.y),(unit.x,unit.y+1),(unit.x,unit.y-1)])
    if len(e_loc & adj) != 0: #checks for enemy aleardy in range
        return #if found skips move and goes to attack phase
    options = inrange(enemies)
    if len(options) == 0: #if no open spaces in range of an enemy are available end turn
        return #moving to attack will end turn if no enemies in range
    nearest = findNearest(unit,options)
    if nearest == (unit.x,unit.y): #only happens if no path to options found
        return #goes to attack which ends turn because no enemy in range
    new_x, new_y = findPath(unit,nearest) 
    grid[unit.y][unit.x] = '.'
    grid[new_y][new_x] = unit.race #these 2 lines move the unit on the grid
    unit.x = new_x
    unit.y = new_y #move the unit in the unit class
    return
    
def attack(unit,enemies):
    global grid
    inrange = []
    for e in [i for i in enemies if i.hp > 0]:
        if e.y == unit.y:
            if e.x == unit.x + 1 or e.x == unit.x - 1:
                inrange.append(e)
        elif e.x == unit.x:
            if e.y == unit.y + 1 or e.y == unit.y - 1:
                inrange.append(e)
    if len(inrange) == 0: #no enemies in range so no attack happens
        return
    inrange.sort(key=lambda e: (e.hp, e.y, e.x)) #sort possible targets by hp then in reading order
    target = inrange[0]
    target.hp -= unit.attack
    if target.hp <= 0: #checks if the attack killed the enemy unit
        grid[target.y][target.x] = '.' #if so remove enemy from grid
    return
    
def solve(puzzle_data):
    global grid
    all_units = puzzle_data
    goblins = [x for x in all_units if x.race == 'G']
    elves = [x for x in all_units if x.race == 'E']
    combat = True
    rounds = 0
    all_units.sort(key=lambda u: (u.y, u.x)) #reduntant but makes sure unit order is correct
    while combat:
        for unit in all_units:
            if unit.hp <= 0:
                continue
            if unit.race == 'G':
                target = elves
            elif unit.race == 'E':
                target = goblins
            if len([t for t in target if t.hp > 0]) == 0:
                combat = False
                break
#            print unit.race, unit.y, unit.x
            move(unit,target) #performs the movement or returns if the unit doesn't move or ends its turn
            attack(unit,target) #attacks the lowest hp unit in range or returns if none in range
        all_units.sort(key=lambda u: (u.y, u.x)) #sort all units into reading order to act next round
        if combat: 
            rounds += 1 #only increment rounds if the round completes
#            print rounds
#        for row in grid:
#            print ''.join(row)
    winners_hp = sum([u.hp for u in all_units if u.hp > 0]) #sum of the hp remaining on all living victors
    return rounds*winners_hp, 0

puzzle_path = "input_day15.txt"
#puzzle_path = "day15_ex6.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
grid, puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
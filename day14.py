# -*- coding: utf-8 -*-
"""
Created on Thu May 12 11:26:48 2022

@author: mjenks
"""
    
def solve(puzzle_data):
    recipes = [3,7]
    elf1 = 0
    elf2 = 1
    while len(recipes) < 10 + puzzle_data:
        new = recipes[elf1] + recipes[elf2]
        for digit in list(str(new)):
            recipes.append(int(digit))
        elf1 = (elf1 + recipes[elf1] + 1)%len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1)%len(recipes)
    return ''.join([str(x) for x in recipes[puzzle_data:puzzle_data+10]]), 0


puzzle_data = 540391
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
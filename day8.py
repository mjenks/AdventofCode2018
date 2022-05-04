# -*- coding: utf-8 -*-
"""
Created on Wed May 04 11:06:18 2022

@author: mjenks
"""

class Node:
    def __init__(self, children, meta):
        self.children = children
        self.num_meta = meta
        self.meta = []

def parse(tree):
    children, meta = tree[:2]
    node = Node(children, meta)
    tree = tree[2:]
    for i in range(children):
        tree = parse(tree)
    node.meta = tree[:meta]
    puzzle_data.append(node)
    return tree[meta:]
    
def solve(puzzle_data):
    return sum([sum(n.meta) for n in puzzle_data]), 0

puzzle_path = "input_day8.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = []
a = parse([int(x) for x in puzzle_input.strip().split()])
solution1, solution2 = solve(puzzle_data)
print len(puzzle_data)
print(solution1)
print(solution2)
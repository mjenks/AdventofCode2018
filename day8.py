# -*- coding: utf-8 -*-
"""
Created on Wed May 04 11:06:18 2022

@author: mjenks
"""

class Node:
    def __init__(self, children, meta):
        self.num_children = children
        self.num_meta = meta
        self.meta = []
        self.children = []
        
    def value(self):
        if self.num_children == 0:
            return sum(self.meta)
        else:
            value = 0
            for i in self.meta:
                if i <= self.num_children:
                    value += self.children[i-1]
                else:
                    value += 0
            return value

def parse(tree):
    children, meta = tree[:2]
    node = Node(children, meta)
    tree = tree[2:]
    for i in range(children):
        tree, child = parse(tree)
        node.children.append(child)
    node.meta = tree[:meta]
    puzzle_data.append(node)
    return tree[meta:], node.value()
    
def solve(puzzle_data):
    return sum([sum(n.meta) for n in puzzle_data])

puzzle_path = "input_day8.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = []
a,b = parse([int(x) for x in puzzle_input.strip().split()])
solution1 = solve(puzzle_data)
solution2 = b

print(solution1)
print(solution2)
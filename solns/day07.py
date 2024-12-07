#!/usr/bin/env python
from itertools import product
sample = False

if sample == True:
    filename = "inputs/day07_sample.txt"
else:
    filename = "inputs/day07.txt"

def parse_input(filename):
    puzzle_input = []
    with open(filename) as f:
        for line in f:
            tgt, ints = line.split(':')
            ints = [int(i) for i in ints.split()]
            puzzle_input.append([int(tgt), ints])
    return puzzle_input

def check_row_pt1(tgt, ints, ops):
    result = ints[0]
    for x, op in zip(ints[1:], ops):
        if op: # True ops = multiply
            result *= x
        else:
            result += x
        if result > tgt:
            return False
    if result == tgt:
        return True
    else:
        return False

def solve_row_pt1(tgt, ints):    
    possible_ops = product([True, False], repeat = len(ints) - 1)
    for ops in possible_ops:
        if check_row_pt1(tgt, ints, ops):
            return True
    return False

def solve_pt1(puzzle_input):
    ans1 = 0
    for line in puzzle_input:
        tgt = line[0]
        ints = line[1]
        if solve_row_pt1(tgt, ints):
            ans1 += tgt
    return ans1

def check_row_pt2(tgt, ints, ops):
    result = ints[0]
    for x, op in zip(ints[1:], ops):
        if op == 0:
            result *= x
        elif op == 1:
            result += x
        else:
            result = int(str(result) + str(x))
        if result > tgt:
            return False
    if result == tgt:
        return True
    else:
        return False

def solve_row_pt2(tgt, ints):    
    possible_ops = product([0, 1, 2], repeat = len(ints) - 1)
    for ops in possible_ops:
        if check_row_pt2(tgt, ints, ops):
            return True
    return False

def solve_pt2(puzzle_input):
    ans2 = 0
    for line in puzzle_input:
        tgt = line[0]
        ints = line[1]
        if solve_row_pt2(tgt, ints):
            ans2 += tgt
    return ans2


puzzle_input = parse_input(filename)
ans_1 = solve_pt1(puzzle_input)
ans_2 = solve_pt2(puzzle_input)

print(ans_1)
print(ans_2)
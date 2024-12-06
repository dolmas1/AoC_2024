#!/usr/bin/env python
import re
sample = False

if sample == True:
    filename = "inputs/day03_sample.txt"
else:
    filename = "inputs/day03.txt"

def read_input(filename):
    with open(filename, 'r') as f:
        puzzle_input = f.read().splitlines()
    return ''.join(puzzle_input)

def censor_input(puzzle_input):
    pattern = r"don\'t\(\).+?do\(\)"
    input_censored = re.sub(pattern, '', puzzle_input)
    return input_censored

def parse_input(puzzle_input):
    pattern = r'mul\((\d{1,3})\,(\d{1,3})\)'
    instructs = re.finditer(pattern, puzzle_input)
    return instructs

def solve(instructs):
    pairs = [list(map(int, m.groups())) for m in instructs]
    return sum([p[0]*p[1] for p in pairs])

puzzle_input = read_input(filename)
puzzle_input_censored = censor_input(puzzle_input)

instructs_pt1 = parse_input(puzzle_input)
instructs_pt2 = parse_input(puzzle_input_censored)
ans1 = solve(instructs_pt1)
ans2 = solve(instructs_pt2)
print(ans1)
print(ans2)
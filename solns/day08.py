#!/usr/bin/env python
from collections import defaultdict
from itertools import combinations

sample = False

if sample == True:
    filename = "inputs/day08_sample.txt"
else:
    filename = "inputs/day08.txt"

def parse_input(filename):
    with open(filename) as f:
        puzzle_input = f.read().splitlines()
    height = len(puzzle_input)
    width = len(puzzle_input[0])
    return puzzle_input, height, width

def find_antennas(puzzle_input):
    antennas = defaultdict(list)
    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char != '.':
                antennas[char].append((i,j))
    return antennas

def check_within_bounds(p, height, width):
    if min(p[0], p[1]) < 0 or p[0] >= height or p[1] >= width:
        return False
    return True

def project_p1(p1, p2, height, width):
    i_diff = p1[0] - p2[0]
    j_diff = p1[1] - p2[1]
    antinode1 = (p1[0] + i_diff, p1[1] + j_diff)
    antinode2 = (p2[0] - i_diff, p2[1] - j_diff)
    return [a for a in [antinode1, antinode2] if check_within_bounds(a, height, width)]

def project_p2(p1, p2, height, width):
    i_diff = p1[0] - p2[0]
    j_diff = p1[1] - p2[1]

    antinodes = []

    # project downwards from p1, until out-of-bounds
    num_steps = 0
    antinode = p1
    while check_within_bounds(antinode, height, width):
        antinodes.append(antinode)
        num_steps += 1
        antinode = (p1[0] + (num_steps * i_diff), p1[1] + (num_steps * j_diff))

    # project upwards from p2, until out-of-bounds
    num_steps = 0
    antinode = p2
    while check_within_bounds(antinode, height, width):
        antinodes.append(antinode)
        num_steps -= 1
        antinode = (p2[0] + (num_steps * i_diff), p2[1] + (num_steps * j_diff))
        
    return antinodes

def find_antinodes(antennas, height, width):
    antinodes_p1 = []
    antinodes_p2 = []
    for k, locs in antennas.items():
        pairs = combinations(locs, 2)
        for (p1, p2) in pairs:
            antinodes_p1 += project_p1(p1, p2, height, width)
            antinodes_p2 += project_p2(p1, p2, height, width)
    return set(antinodes_p1), set(antinodes_p2)

def solve(filename):
    puzzle_input, height, width = parse_input(filename)

    antennas = find_antennas(puzzle_input)
    
    antinodes_p1, antinodes_p2 = find_antinodes(antennas, height, width)
    return(len(antinodes_p1), len(antinodes_p2))


ans_1, ans_2 = solve(filename)
print(ans_1)
print(ans_2)
#!/usr/bin/env python
sample = False

if sample == True:
    filename = "inputs/day11_sample.txt"
else:
    filename = "inputs/day11.txt"

from collections import defaultdict

def parse_input(filename):
    with open(filename) as f:
        puzzle_input = []
        for line in f.readlines():
            puzzle_input += line.split()
    return [int(s) for s in puzzle_input]


def process_stone(stone):
    if stone == 0:
        return [1]
    else:
        str_stone = str(stone)
        l = len(str_stone)
        if (l % 2) == 0:
            split = int(l/2)
            return [int(str_stone[:split]), int(str_stone[split:])]
        else:
            return [int(stone)*2024]

def process_line(current_state, memory):
    new_state = defaultdict(int)
    for stone, reps in current_state.items():
        
        if stone not in memory.keys():
            memory[stone] = process_stone(stone)
        new_stones = memory[stone]
        for s in new_stones:
            new_state[s] += reps
    return new_state, memory

def solve(filename):
    puzzle_input = parse_input(filename)
    current_state = defaultdict(int)
    for stone in puzzle_input:
        current_state[stone] += 1
    memory = {}
    ans = []
    for i in range(75):
        current_state, memory = process_line(current_state, memory)
        if i == 24:
            ans.append(sum([k for k in current_state.values()]))
        if i == 74:
            ans.append(sum([k for k in current_state.values()]))
    return ans

[ans_1, ans_2] = solve(filename)

print(ans_1)
print(ans_2)
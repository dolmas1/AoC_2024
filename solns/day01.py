#!/usr/bin/env python
from collections import Counter

sample = 0

if sample == True:
    filename = "inputs/day01_sample.txt"
else:
    filename = "inputs/day01.txt"

def parse_input(filename):
    # read it all the data first...
    with open(filename) as f:
        puzzle_input = f.read().splitlines()
    # then process it
    l1, l2 = [], []
    for line in puzzle_input:
        num1, num2 = map(int, line.split())
        l1.append(num1)
        l2.append(num2)
    l1.sort()
    l2.sort()
    return l1, l2

def solve_pt1(l1, l2):
    diffs = [abs(a - b) for a,b in zip(l1, l2)]
    return sum(diffs)

def solve_pt2(l1, l2):
    ans = 0
    counts = Counter(l2)
    for val in l1:
        ans += val * counts[val]
    return ans

l1, l2 = parse_input(filename)
ans_1 = solve_pt1(l1, l2)
ans_2 = solve_pt2(l1, l2)

print(ans_1)
print(ans_2)
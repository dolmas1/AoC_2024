#!/usr/bin/env python
from collections import Counter

sample = 0

if sample == True:
    filename = "inputs/day02_sample.txt"
else:
    filename = "inputs/day02.txt"

def parse_input(filename):
    with open(filename) as f:
        puzzle_input = f.read().splitlines()
    reports = [list(map(int, line.split())) for line in puzzle_input]
    return reports

def solve_line(report):
    sorted_report = sorted(report)
    if (sorted_report != report) and (sorted_report[::-1] != report):
        return False
    diffs = []
    for v1, v2 in zip(sorted_report, sorted_report[1:]):
        diffs.append(v1 - v2)
    diff_set = set(diffs)
    if diff_set.issubset(set([-1,-2,-3])):
        return True
    else:
        return False

def solve_line2(report):
    if solve_line(report):
        return (True, True)
    else:
        for i in range(len(report)):
            adjust_report = report.copy()
            del adjust_report[i]
            if solve_line(adjust_report):
                return (False, True)
    return (False, False)

reports = parse_input(filename)
validity = list(zip(*map(solve_line2, reports)))
ans_1 = sum(validity[0])
ans_2 = sum(validity[1])

print(ans_1)
print(ans_2)
#!/usr/bin/env python
from collections import defaultdict
sample = False

if sample == True:
    filename = "inputs/day05_sample.txt"
else:
    filename = "inputs/day05.txt"

def read_input(filename):
    with open(filename, 'r') as f:
        rules = []
        updates = []
        input_status = 0
        for line in f:
            if line == '\n':
                input_status = 1
                continue
            elif input_status == 0:
                rule = {}
                rule['rule'] = line.rstrip().split('|')
                rule['pageset'] = set(rule['rule'])
                rules.append(rule)
            else:
                update = {}
                update['update'] = line.rstrip().split(',')
                update['pageset'] = set(update['update'])
                update['middle'] = update['update'][int((len(update['update']) - 1) / 2)]
                updates.append(update)

    return rules, updates

def find_relevant_rules(update, rules):
    return [rule for rule in rules if rule['pageset'].issubset(update['pageset'])]

def check_rule(update, rule):
    if update['update'].index(rule['rule'][0]) < update['update'].index(rule['rule'][1]):
        return True
    else:
        return False

def check_update(update, rules):
    relevant_rules = find_relevant_rules(update, rules)
    for rule in relevant_rules:
        if check_rule(update, rule):
            pass
        else:
            return False
    return True

def solve(updates, rules):
    ans_1 = 0
    ans_2 = 0

    # ordering = defaultdict(int)
    # for rule in rules:
    #     a, b = (rule['rule'][0], rule['rule'][1])
    #     ordering[a] = ordering[b] - 1

    for update in updates:
        if check_update(update, rules):
            ans_1 += int(update['middle'])
        else:

            ordering = defaultdict(int)
            sorting_done = False
            relevant_rules = find_relevant_rules(update, rules)
            while not sorting_done:
                ordering_new = ordering.copy()
                for rule in relevant_rules:
                    a, b = (rule['rule'][0], rule['rule'][1])
                    ordering_new[a] = min(ordering_new[a], ordering_new[b] - 1)
                if ordering_new == ordering:
                    sorting_done = True
                ordering = ordering_new.copy()


            keys = list(map(ordering.get, update['update']))
            sorted_update = [item for _, item in sorted(zip(keys, update['update']))]
            
            ans_2 += int(sorted_update[int((len(sorted_update) - 1) / 2)])
            
    return ans_1, ans_2


rules, updates = read_input(filename)

ans1, ans2 = solve(updates, rules)
print(ans1)
print(ans2)
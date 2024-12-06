#!/usr/bin/env python
sample = False

if sample == True:
    filename = "inputs/day04_sample.txt"
else:
    filename = "inputs/day04.txt"

def read_input(filename):
    with open(filename, 'r') as f:
        puzzle_input = [line.strip() for line in f]
    return puzzle_input

def parse_input(puzzle_input, pattern_length = 4):
    width = len(puzzle_input[0])
    height = len(puzzle_input)

    # Left to right, and right to left
    hor_lr = puzzle_input.copy()
    hor_rl = [s[::-1] for s in hor_lr]

    # Up-down, and down to up
    ver_lr = [''.join(s) for s in list(zip(*puzzle_input))]
    ver_rl = [s[::-1] for s in ver_lr]

    # Diagonal, top-left to bottom-right
    diag_1_upper = [l[i:].ljust(width, ' ') for i, l in enumerate(hor_lr)]
    diag_1_upper = [''.join(s) for s in list(zip(*diag_1_upper))]
    diag_1_lower = [l[:i+1].rjust(width-1, ' ') for i, l in enumerate(hor_lr[1:])]
    diag_1_lower = [''.join(s) for s in list(zip(*diag_1_lower))]
    diag_1 = [s.strip() for s in diag_1_upper + diag_1_lower if len(s.strip()) >= pattern_length]

    # Diagonal, top-right to bottom-left
    diag_2_upper = [l[i:].ljust(width, ' ') for i, l in enumerate(hor_rl)]
    diag_2_upper = [''.join(s) for s in list(zip(*diag_2_upper))]
    diag_2_lower = [l[:i+1].rjust(width-1, ' ') for i, l in enumerate(hor_rl[1:])]
    diag_2_lower = [''.join(s) for s in list(zip(*diag_2_lower))]
    diag_2 = [s.strip() for s in diag_2_upper + diag_2_lower if len(s.strip()) >= pattern_length]

    # Diagonal, bottom-right to top-left
    diag_3 = [s[::-1] for s in diag_1]

    # Diagonal, bottom-left to top-right
    diag_4 = [s[::-1] for s in diag_2]

    all_directions = hor_lr + hor_rl + ver_lr + ver_rl + diag_1 + diag_2 + diag_3 + diag_4

    return all_directions

def find_centres(puzzle_input, centre_char = 'A'):
    centres = []
    for i in range(1, len(puzzle_input) - 1):
        for j in range(1, len(puzzle_input[0]) - 1):
            if puzzle_input[i][j] == centre_char:
                centres.append((i,j))
    return centres

def check_square(puzzle_input, centre):
    (i, j) = centre
    diag1 = puzzle_input[i-1][j-1] + puzzle_input[i+1][j+1]
    diag2 = puzzle_input[i+1][j-1] + puzzle_input[i-1][j+1]
    diag3 = diag1[::-1]
    diag4 = diag2[::-1]
    
    if 'MS' in [diag1, diag3] and 'MS' in [diag2, diag4]:
        return True
    else:
        return False

def solve_pt1(puzzle_input, pattern = 'XMAS'):
    all_directions = parse_input(puzzle_input, len(pattern))
    ans_1 = 0
    for line in all_directions:
        ans_1 += line.count(pattern)
    return ans_1

def solve_pt2(puzzle_input):
    centres = find_centres(puzzle_input)
    return sum([check_square(puzzle_input, centre) for centre in centres])

puzzle_input = read_input(filename)
ans1 = solve_pt1(puzzle_input)
ans2 = solve_pt2(puzzle_input)
print(ans1)
print(ans2)
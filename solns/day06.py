#!/usr/bin/env python
sample = False

if sample == True:
    filename = "inputs/day06_sample.txt"
else:
    filename = "inputs/day06.txt"

with open(filename) as f:
    puzzle_input = f.read().splitlines()

def get_front_coords(current_loc, current_dir):
    i, j = current_loc
    if current_dir == 0: # looking up
        return (i - 1, j)
    elif current_dir == 1: # looking right
        return (i, j + 1)
    elif current_dir == 2: # looking down
        return (i + 1, j)
    elif current_dir == 3: # looking left
        return (i, j - 1)

def out_of_bounds(loc, width = len(puzzle_input[0]), height = len(puzzle_input)):
    i, j = loc
    if i < 0 or i+1 > height or j < 0 or j+1 > width:
        return True
    else:
        return False

def step(puzzle_input, current_loc, current_dir, done):

    alternate_state = None
    front_coords = get_front_coords(current_loc, current_dir)

    # if walking forwards will exit the grid, we are done
    if out_of_bounds(front_coords):
        done = True
        return current_loc, current_dir, done, alternate_state

    # if obstacle in front, stay still but turn to the right
    elif puzzle_input[front_coords[0]][front_coords[1]] == '#':
        return current_loc, (current_dir + 1)%4, done, alternate_state

    # else, walk forward
    else:
        alternate_state = (current_loc, (current_dir + 1)%4) # what would've happened if there WAS an obstacle
        return front_coords, current_dir, done, alternate_state

def check_for_loop(puzzle_input, loc, facing, previous_states):

    visited_states = previous_states.copy()

    done = False
    while not done:
        if (loc, facing) in visited_states:
            return True
        else:
            visited_states.append((loc, facing))
            loc, facing, done, _ = step(puzzle_input, loc, facing, done)
            
    return False

def solve(puzzle_input):
    # Set up initial conditions
    loc = (0, 0)
    for i, line in enumerate(puzzle_input):
        if '^' in line:
            loc = (i, line.index('^'))
    
    facing = 0
    done = False
    
    # Walk the grid
    visited_squares = []
    visited_states = []
    potential_blockers = []
    definite_blockers = []
    while not done:
        visited_squares.append(loc)
        visited_states.append((loc, facing))
        potential_blocker = get_front_coords(loc, facing)
        
        loc, facing, done, alternate_state = step(puzzle_input, loc, facing, done)
        
        if alternate_state and (potential_blocker not in potential_blockers):
            
            potential_blockers.append(potential_blocker)
            
            # Add blocker to alternative version of puzzle input
            hypothetical_puzzle = puzzle_input.copy()
            new_line = hypothetical_puzzle[loc[0]]
            new_line = new_line[:loc[1]] + '#' + new_line[loc[1]+1:]
            hypothetical_puzzle[loc[0]] = new_line
            
            # see if following the path from current point would lead to loop
            if check_for_loop(hypothetical_puzzle, alternate_state[0], alternate_state[1], visited_states):
                definite_blockers.append(potential_blocker)
    
    ans_1 = len(set(visited_squares))
    ans_2 = len(set(definite_blockers))

    return ans_1, ans_2

ans1, ans2 = solve(puzzle_input)
print(ans1)
print(ans2)
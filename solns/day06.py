#!/usr/bin/env python
sample = False

if sample == True:
    filename = "inputs/day06_sample.txt"
else:
    filename = "inputs/day06.txt"

def parse_data(filename):
    with open(filename) as f:
        puzzle_input = f.read().splitlines()
        #puzzle_input = [list(s) for s in puzzle_input]
    
    starting_loc = (0, 0)
    for i, line in enumerate(puzzle_input):
        if '^' in line:
            starting_loc = (i, line.index('^'))
            
    return puzzle_input, starting_loc

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

def out_of_bounds(loc, width, height):
    i, j = loc
    if i < 0 or i+1 > height or j < 0 or j+1 > width:
        return True
    else:
        return False

def step(puzzle_input, current_loc, current_dir, done):

    alternate_state = None
    front_coords = get_front_coords(current_loc, current_dir)

    # if walking forwards will exit the grid, we are done
    if out_of_bounds(front_coords, width = len(puzzle_input[0]), height = len(puzzle_input)):
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
            visited_states.add((loc, facing))
            loc, facing, done, _ = step(puzzle_input, loc, facing, done)
            
    return False

def solve_pt1(puzzle_input, starting_loc):
    # Set up initial conditions
    loc = starting_loc
    facing = 0
    done = False
    
    # Walk the grid
    visited_squares = set()

    while not done:
        visited_squares.add(loc)
        loc, facing, done, _ = step(puzzle_input, loc, facing, done)
        
    
    ans_1 = len(visited_squares)

    return ans_1, visited_squares

def solve_pt2(puzzle_input, starting_loc, visited_pt1):
    # Set up initial conditions
    loc = starting_loc
    facing = 0
    done = False
    
    # Walk the grid
    visited_squares = set()
    visited_states = set()
    potential_blockers = set()
    definite_blockers = set()
    while not done:
        visited_squares.add(loc)
        
        visited_states.add((loc, facing))
        potential_blocker = get_front_coords(loc, facing)
        
        loc, facing, done, alternate_state = step(puzzle_input, loc, facing, done)
        
        if alternate_state and (potential_blocker not in potential_blockers) and (potential_blocker not in visited_squares) and (potential_blocker in visited_pt1):
            
            potential_blockers.add(potential_blocker)
            
            # Add blocker to alternative version of puzzle input
            hypothetical_puzzle = puzzle_input.copy()
            #hypothetical_puzzle[loc[0]][loc[1]] = '#'
            new_line = hypothetical_puzzle[loc[0]]
            new_line = new_line[:loc[1]] + '#' + new_line[loc[1]+1:]
            hypothetical_puzzle[loc[0]] = new_line
            
            # see if following the path from current point would lead to loop
            if check_for_loop(hypothetical_puzzle, alternate_state[0], alternate_state[1], visited_states):
                definite_blockers.add(potential_blocker)
    
    ans_2 = len(definite_blockers)

    return ans_2


puzzle_input, starting_loc = parse_data(filename)

ans_1, visited_pt1 = solve_pt1(puzzle_input, starting_loc)
ans_2 = solve_pt2(puzzle_input, starting_loc, visited_pt1)
print(ans_1)
print(ans_2)
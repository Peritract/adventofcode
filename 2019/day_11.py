import math
from int_code_computer import IntCodeComputer

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

def get_grid_colour(locations, location):
    if location not in locations.keys():
        locations[location] = 0
    return locations[location]

def paint_location(locations, location, colour):
    locations[location] = colour

def move_robot(current, heading, instruction):
    new_loc = (0,0)
    new_heading = ""
    lefts = {"N": "W", "S": "E", "E": "N", "W": "S"}
    rights = {"W": "N", "E": "S", "N": "E", "S": "W"}
    moves = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
    if instruction == 0:
        new_heading = lefts[heading]
    else:
        new_heading = rights[heading]
    new_loc = (current[0] + moves[new_heading][0],
               current[1] + moves[new_heading][1])
    return new_loc, new_heading

def paint_sign(data, starting_point):
    robot = IntCodeComputer(data)
    location = starting_point[0]
    orientation = "N"
    locations = {starting_point[0]: starting_point[1]}
    while not robot.halt:
        robot.add_input(get_grid_colour(locations, location))
        robot.run()
        paint_location(locations, location, robot.output_log[-2])
        location, orientation = move_robot(location, orientation, robot.output_log[-1])
    return locations

def first_star(data):
    locations = paint_sign(data, [(0,0), 0])
    return len(set(locations.keys()))

def second_star(data):
    locations = paint_sign(data, [(0,0), 1])
    grid = [[" " for y in range(41)] for y in range(6)]
    for loc in locations.keys():
        if locations[loc] == 1:
            grid[loc[0]][loc[1]] = "#"
    for line in grid:
        print("".join(line))

def solution(source):
    data = load_input(source)
    data = [int(x) for x in data.split(",")]
    print("Day 11")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    

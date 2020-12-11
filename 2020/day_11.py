# I got lost on this one and needed to call out for help; the code is mine but the concept wasn't.

from functools import reduce

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [[y for y in x.strip()] for x in file.readlines()]

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0),
        (1, 1), (-1, -1), (-1, 1), (1, -1)]
    
    
def adjacent(data, y, x):
    seat = data[y][x]
    count = 0
    for dir in dirs:
        ny = y + dir[0]
        nx = x + dir[1]
        if valid(data, ny, nx): 
            if data[ny][nx] == "#":
                count += 1
    return count

def toggle(val, adj, lim=4):
    if val == ".":
        return val
    elif adj == 0 and val == "L":
        return "#"
    elif adj >= lim and val == "#":
        return "L"
    else:
        return val
    
def display(grid):
    for x in grid:
        print("".join(x))
    print("-------------")
    
def first_star(grid):
    #display(grid)
    swap = True
    rounds = 0
    while swap == True:
        rounds += 1
        swap = False
        new_grid = []
        for row in range(len(grid)):
            n_row = []
            for seat in range(len(grid[0])):
                val = grid[row][seat]
                adj = adjacent(grid, row, seat)
                tog = toggle(val, adj)
                n_row.append(tog)
                if tog != val:
                    swap = True
            new_grid.append(n_row)
        grid = new_grid
        #display(grid)
    return sum([x.count("#") for x in grid])

def valid(data, y, x):
    return 0 <= y < len(data) and 0 <= x < len(data[0])

def walk_line(data, y, x, dir):
    ny = y + dir[0]
    nx = x + dir[1]
    while valid(data, ny, nx):
        if data[ny][nx] == "#":
            return 1
        elif data[ny][nx] == "L":
            return 0
        else:
            ny = ny + dir[0]
            nx = nx + dir[1]
    else:
        return 0

def visible(data, y, x):
    t = data[y][x]
    vis = 0
    for dir in dirs:
        vis += walk_line(data, y, x, dir)
    return vis

def second_star(grid):
    swap = True
    rounds = 0
    while swap == True:
        rounds += 1
        swap = False
        new_grid = []
        for row in range(len(grid)):
            n_row = []
            for seat in range(len(grid[0])):
                val = grid[row][seat]
                adj = visible(grid, row, seat)
                tog = toggle(val, adj, 5)
                n_row.append(tog)
                if tog != val:
                    swap = True
            new_grid.append(n_row)
        grid = new_grid
    return sum([x.count("#") for x in grid])
    
def solution(source):
    data = load_input(source)
    print("Day 11")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

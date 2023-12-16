from functools import cmp_to_key
from collections import defaultdict

def load_input(source):
    with open(source) as f:
        data = [list(x.strip()) for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data

def display_grid(grid):
    for y in grid:
        print("".join(y))
    print("")


def tilt_west(grid):
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(grid[0])):
            if row[x] == "O":
                o = x - 1
                while row[o] == "." and o >= 0:
                    o -= 1
                row[o + 1], row[x] = row[x], row[o + 1]
    return grid


def tilt_east(grid):
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(grid[0]) - 1, -1, -1):
            if row[x] == "O":
                o = x + 1
                while o < len(grid[0]) and row[o] == ".":
                    o += 1
                row[o - 1], row[x] = row[x], row[o - 1]
    return grid


def tilt_north(grid):
    cols = []
    for c in range(len(grid[0])):
        col = [y[c] for y in grid]
        for x in range(len(col)):
            if col[x] == "O":
                o = x - 1
                while col[o] == "." and o >= 0:
                    o -= 1
                col[o + 1], col[x] = col[x], col[o + 1]
        cols.append(col)
    n_grid = []
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[0])):
            row += cols[x][y]
        n_grid.append(list(row))
    return n_grid
    

def tilt_south(grid):
    cols = []
    for c in range(len(grid[0])):
        col = [y[c] for y in grid]
        for x in range(len(col) -1, -1, -1):
            if col[x] == "O":
                o = x + 1
                while o < len(col) and col[o] == ".":
                    o += 1
                col[o - 1], col[x] = col[x], col[o - 1]
        cols.append(col)
    n_grid = []
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[0])):
            row += cols[x][y]
        n_grid.append(list(row))
    return n_grid


def spin(grid):
    for func in [tilt_north, tilt_west, tilt_south, tilt_east]:
        grid = func(grid)
    return grid


def string_rep(grid):
    return "|".join("-".join(y) for y in grid)

def reconstruct(sr):
    return [r.split("-") for r in sr.split("|")]

def first_star(data):
    grid = tilt_north(data)
    tot = sum([r.count("O") * (len(grid) - i)
           for i, r in enumerate(grid)])

    return tot


def second_star(data):
    grid = data
    grids = []
    dupes = defaultdict(lambda: [])
    for i in range(1000):
        grid = spin(grid)
        sr = string_rep(grid)
        if sr not in grids:
            grids.append(sr)
        else:
            dupes[grids.index(sr)].append(i)
    start = list(dupes.keys())[0]
    step = [v[1] - v[0] for v in dupes.values()][0]
    to_run = 1000000000 - start - 1
    grid = data
    for i in range(start):
        grid = spin(grid)
    patterns = []
    for c in range(0, len(dupes.keys())):
        grid = spin(grid)
        patterns.append(string_rep(grid))
        tot = sum([r.count("O") * (len(grid) - i)
           for i, r in enumerate(grid)])
    result = reconstruct(patterns[to_run % len(patterns)])
    tot = sum([r.count("O") * (len(result) - i)
        for i, r in enumerate(result)])

    return tot

def solution(source):
    data = load_input(source)
    print("Day 14")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

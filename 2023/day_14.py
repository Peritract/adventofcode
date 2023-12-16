from functools import cmp_to_key

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data

def display_grid(grid):
    for y in grid:
        print("".join(y))
    print("")

def sort_rocks(b, a):
    if b == "O" and a == ".":
        return -1
    elif b == "." and a == "O":
        return 1
    return 0

def roll(grid, dir):
    if dir == "W":
        return [sorted(row,
                key=cmp_to_key(sort_rocks))
                for row in grid]
    elif dir == "E":
        return [sorted(row[::-1],
                key=cmp_to_key(sort_rocks))[::-1]
                for row in grid]


def rotate(grid):
    n_grid = []
    for x in range(len(grid[0])):
        n_grid.append([grid[y][x] for y in range(len(grid))])
    return n_grid

   
def tilt(grid):
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
        n_grid.append(row)
    return n_grid
    
def first_star(data):
    grid = tilt(data)
    tot = sum([r.count("O") * (len(grid) - i)
           for i, r in enumerate(grid)])

    return tot


def second_star(data):
    display_grid(roll(data, "W"))
    display_grid(roll(data, "E"))


def solution(source):
    data = load_input(source)
    print("Day N")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

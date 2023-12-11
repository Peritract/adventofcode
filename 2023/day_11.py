from itertools import combinations

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data


def expand(data):
    taller = []
    for row in data:
        if row.count(".") == len(row):
            taller.append([x for x in row])
        taller.append(row)
    wider = ["" for y in taller]
    for x in range(len(data[0])):
        col = [y[x] for y in taller]
        for y in range(len(taller)):
            wider[y] += col[y]
        if col.count(".") == len(col):
            for y in range(len(taller)):
                wider[y] += "."

    return wider


def find_expansions(data):
    rows = []
    cols = []
    for r in range(len(data)):
        if data[r].count(".") == len(data[r]):
            rows.append(r)
    for x in range(len(data[0])):
        col = [y[x] for y in data]
        if col.count(".") == len(col):
            cols.append(x)
    return rows, cols


def display_grid(grid):
    for y in grid:
        print("".join(y))
    print("")


def locate_galaxies(space):
    galaxies = []
    for y in range(len(space)):
        for x in range(len(space[0])):
            if space[y][x] == "#":
                galaxies.append((x, y))
    return galaxies


def get_manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_expanded_manhattan_dist(a, b, rows, cols, offset):
    base = abs(a[0] - b[0]) + abs(a[1] - b[1])
    start_x, end_x = min((a[0], b[0])), max((a[0], b[0]))
    start_y, end_y = min((a[1], b[1])), max((a[1], b[1]))
    row_count = len([y for y in rows if start_y < y < end_y])
    col_count = len([x for x in cols if start_x < x < end_x])
    total_expansions = row_count + col_count
    increment = (total_expansions * offset) - total_expansions if total_expansions else 0
    return base + increment


def first_star(data):
    space = expand(data)
    galaxies = locate_galaxies(space)
    pairs = combinations(galaxies, 2)
    return sum([get_manhattan_dist(a, b)
                for a, b in pairs])


def second_star(data):
    rows, cols = find_expansions(data)
    galaxies = locate_galaxies(data)
    pairs = combinations(galaxies, 2)
    return sum([get_expanded_manhattan_dist(a, b, rows, cols, 1000000)
                for a, b in pairs])


def solution(source):
    data = load_input(source)
    print("Day 11")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

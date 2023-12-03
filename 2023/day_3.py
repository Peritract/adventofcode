import re
from collections import defaultdict
from functools import reduce
from operator import mul


def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data


def get_neighbours(num, start_y, max_x, max_y):
    coords = tuple((x, start_y) for x in range(*num.span()))
    neighbours = set()
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for c in coords:
                dx = c[0] + x
                dy = c[1] + y
                if (dx, dy) not in coords and (0 <= dx <= max_x) and (0 <= dy <= max_y):
                    neighbours.add((dx, dy))
    return neighbours


def has_adjacent_symbol(grid, neighbours):
    for n in neighbours:
        cell = grid[n[1]][n[0]]
        if cell != "." and not cell.isdigit():
            return cell
    return False


def get_adjacent_gears(grid, neighbours):
    gears = []
    for n in neighbours:
        cell = grid[n[1]][n[0]]
        if cell  == "*":
            gears.append((n[0], n[1]))
    return gears


def first_star(data):
    max_x = len(data[0]) - 1
    max_y = len(data) - 1
    part_sum = 0
    for y in range(len(data)):
        for num in re.finditer("(\d+)", data[y]):
            n = get_neighbours(num, y, max_x, max_y)
            if has_adjacent_symbol(data, n):
                part_sum += int(num.group())
    return part_sum


def second_star(data):
    max_x = len(data[0]) - 1
    max_y = len(data) - 1
    gears = defaultdict(list)
    gear_score = 0
    for y in range(len(data)):
        for num in re.finditer("(\d+)", data[y]):
            d = int(num.group())
            n = get_neighbours(num, y, max_x, max_y)
            for g in get_adjacent_gears(data, n):
                gears[g].append(d)
    for v in gears.values():
        if len(v) > 1:
            gear_score += reduce(mul, v, 1)
    return gear_score


def solution(source):
    data = load_input(source)
    print("Day 3")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

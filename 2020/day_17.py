from collections import defaultdict
from copy import deepcopy

def load_input(source="input.txt", dim=3):
    points = defaultdict(lambda: 0)
    with open(source, 'r') as file:
        text = file.read()
    rows = text.split("\n")
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            points[(0, y, x)] = 0 if rows[y][x] == '.' else 1

    return points

def get_neighbour_coords():
    coords = []
    for z in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            for x in range(-1, 2, 1):
                if (z, y, x) != (0, 0, 0):
                    coords.append((z, y, x))
    return coords

def tuple_add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def poll(data, point, neighbours):
    """Returns the number of nearby active cubes"""
    active = 0
    for n in neighbours:
        coord = tuple_add(point, n)
        active += data[coord]
    return active

def display(points, dist, size):
    for layer in range(-dist, dist + 1, 1):
        print(f"Z = {layer}")
        for y in range(-size, size + 1, 1):
            for x in range(-size, size + 1, 1):
                print(points[(layer, y, x)], end="")
            print("")
        print("-" * 8)

def total(points):
    return sum(points[x] for x in points.keys())

def first_star(data):
    points = data
    nearby = get_neighbour_coords()
    for i in range(6):
        for point in list(points.keys()):
            count = poll(points, point, nearby)
    cycles = 0
    while cycles < 6:
        new_points = deepcopy(points)
        for point in list(points.keys()):
            count = poll(points, point, nearby)
            if points[point] == 1:
                new_points[point] = 1 if count in (2, 3) else 0
            else:
                new_points[point] = 1 if count == 3 else 0
        points = new_points
        cycles += 1
    
    return total(points)

def get_hyper_neighbours():
    coords = []
    for z in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            for x in range(-1, 2, 1):
                for w in range(-1, 2, 1):
                    if (z, y, x, w) != (0, 0, 0, 0):
                        coords.append((z, y, x, w))
    return coords

def second_star(data):
    points = defaultdict(lambda: 0)
    for point in data:
        hyper_coord = point + tuple([0])
        points[hyper_coord] = data[point]
    nearby = get_hyper_neighbours()
    for i in range(6):
        for point in list(points.keys()):
            count = poll(points, point, nearby)
    cycles = 0
    while cycles < 6:
        new_points = deepcopy(points)
        for point in list(points.keys()):
            count = poll(points, point, nearby)
            if points[point] == 1:
                new_points[point] = 1 if count in (2, 3) else 0
            else:
                new_points[point] = 1 if count == 3 else 0
        points = new_points
        cycles += 1
        
    return total(points)
    
def solution(source):
    data = load_input(source)
    print("Day 17")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

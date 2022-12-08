from math import ceil
from functools import reduce

def load_input(filename):
  with open(filename) as f_obj:
    return [[{'val': int(y), 'vis': 0, 'vis_from': [], 'vis_score': 0} for y in x.strip()] for x in f_obj.readlines()]

def assess_march_visibility(x, y, grid, obj):
    routes = []
    for n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        route = True
        nx, ny = x + n[0], y + n[1]
        while nx >= 0 and ny >= 0 and nx < len(grid[0]) and ny < len(grid):
            adj = grid[ny][nx]
            if adj['val'] >= obj['val']:
                route = False
            nx, ny = nx + n[0], ny + n[1]
        if route == True:
            routes.append(n)
    obj['vis_from'] = routes
    if len(routes) > 0:
        obj['vis'] = 1
    return obj

def display_grid_feature(grid, feature):
    for y in grid:
        print("".join([str(x[feature]) for x in y]))

def first_star(data):
    for y in range(len(data)):
        for x in range(len(data[0])):
            data[y][x] = assess_march_visibility(x, y, data, data[y][x])
    count = 0
    for y in data:
        for x in y:
            count += x['vis']
    return count

def get_visibility_score(x, y, grid, obj):
    scores = []
    for n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        vis = 0
        blocked = False
        nx, ny = x + n[0], y + n[1]
        while nx >= 0 and ny >= 0 and nx < len(grid[0]) and ny < len(grid) and not blocked:
            adj = grid[ny][nx]
            vis += 1
            if adj['val'] >= obj['val']:
                blocked = True
            nx, ny = nx + n[0], ny + n[1]
        scores.append(vis)
    obj['vis_score'] = reduce(lambda a, b: a * b, scores)
    return obj

def second_star(data):
    lrg = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            data[y][x] = get_visibility_score(x, y, data, data[y][x])
            if data[y][x]['vis_score'] > lrg:
                lrg = data[y][x]['vis_score']
    return lrg

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

from collections import defaultdict

def load_input(source):
    with open(source) as f:
        data = [[int(x) for x in y.strip()] for y in f.readlines()]
    return data

def get_trailheads(grid):
    trailheads = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                trailheads.append((x, y))
    return trailheads

def get_graph(grid):
    nodes = defaultdict(lambda: {'v': None, 'l': []})
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            val = grid[y][x]
            nodes[(x, y)]['v'] = val
            for dir in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nx, ny = x + dir[0], y + dir[1]
                if (0 <= nx < len(grid[0])) and (0 <= ny < len(grid)): 
                    if grid[ny][nx] == val + 1:
                        nodes[(x, y)]['l'].append((nx, ny))
    return nodes

def get_dests(loc, graph):
    if graph[loc]['v'] == 9:
        return loc
    else:
        dests = [
            get_dests(l, graph)
            for l in graph[loc]['l']
        ]
        flat_dests = []
        for x in dests:
            if isinstance(x, tuple):
                flat_dests.append(x)
            else:
                flat_dests.extend(x)
        return flat_dests

def get_routes(loc, graph, so_far=None):
    so_far = so_far if so_far else []
    if graph[loc]['v'] == 9:
        so_far.append(loc)
        return tuple(so_far)
    else:
        so_far.append(loc)
        dests = [
            get_routes(l, graph, [x for x in so_far])
            for l in graph[loc]['l']
        ]
        flat_dests = []
        for x in dests:
            if isinstance(x, tuple):
                flat_dests.append(x)
            else:
                flat_dests.extend(x)
        return flat_dests

def first_star(data):
    trailheads = get_trailheads(data)
    g = get_graph(data)
    tot = 0
    for t in trailheads:
        tot += len(set(get_dests(t, g)))
    return tot

def second_star(data):
    trailheads = get_trailheads(data)
    g = get_graph(data)
    tot = 0
    for t in trailheads:
        tot += len(set(get_routes(t, g)))
    return tot

def solution(source):
    data = load_input(source)
    print("Day 10")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

from collections import defaultdict

def load_input(source):
    with open(source) as f:
        data = [l.strip() for l in f.readlines()]
    return data

def is_in_bounds(l, x, y):
    return (0 <= l[0] < x) and (0 <= l[1] < y)

def get_antinodes(a, b, max_x, max_y):
    dx, dy = a[0] - b[0], a[1] - b[1]
    locs = ((b[0] - dx, b[1] - dy), (a[0] + dx, a[1] + dy))
    return [l for l in locs if is_in_bounds(l, max_x, max_y)]

def get_marching_antinodes(a, b, max_x, max_y):
    dx, dy = a[0] - b[0], a[1] - b[1]
    cax, cay = a
    bax, bay = b
    locs = [a, b]
    while(is_in_bounds((cax, cay), max_x, max_y)):
        cax, cay = cax + dx, cay + dy
        locs.append((cax, cay))
    while(is_in_bounds((bax, bay), max_x, max_y)):
        bax, bay = bax - dx, bay - dy
        locs.append((bax, bay))
    print(a, b, locs)
    return [l for l in locs if is_in_bounds(l, max_x, max_y)]

def first_star(data):
    max_x, max_y = len(data[0]), len(data)
    antenna = defaultdict(lambda: [])
    for x in range(len(data[0])):
        for y in range(len(data)):
            if data[y][x] != '.':
                antenna[data[y][x]].append((x, y))
    antinodes = []
    for a_type, locs in antenna.items():
        for i in range(len(locs) - 1):
            for j in range(i+1, len(locs)):
                antinodes.extend(get_antinodes(locs[i], locs[j], max_x, max_y))
    return len(set(antinodes))

def second_star(data):
    max_x, max_y = len(data[0]), len(data)
    antenna = defaultdict(lambda: [])
    for x in range(len(data[0])):
        for y in range(len(data)):
            if data[y][x] != '.':
                antenna[data[y][x]].append((x, y))
    antinodes = []
    for a_type, locs in antenna.items():
        for i in range(len(locs) - 1):
            for j in range(i+1, len(locs)):
                antinodes.extend(get_marching_antinodes(locs[i], locs[j], max_x, max_y))
    return len(set(antinodes))


def solution(source):
    data = load_input(source)
    print("Day 8")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

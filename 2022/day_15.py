import re
from collections import defaultdict

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data
    
def parse_coord_line(line):
    coords = [int(x) for x in re.findall("-?\d+", line)]
    return tuple(coords[:2]), tuple(coords[2:])

class Sensor:

    def __init__(self, loc, nearest_beacon):
        self.loc = loc
        self.beacon = nearest_beacon
        self.dist = self.get_manhattan_distance(self.beacon)

    def __repr__(self):
        return f"{self.loc}: {self.dist}"

    def get_manhattan_distance(self, other):
        return abs(other[0] - self.loc[0]) + abs(other[1] - self.loc[1])
    
    def reachable(self, other):
        if self.get_manhattan_distance(other) <= self.dist:
            return True
    
        return False
    
    def reachable_on_y(self, y, lim=None, x_only=False):
        if self.dist < abs(self.loc[1] - y):
            return []
        else:
            locs = []
            x_dist = self.dist - abs(self.loc[1] - y)
            for dx in range(-x_dist, x_dist + 1):
                nx = dx + self.loc[0]
                if lim:
                    if 0 <= nx and nx <= lim and 0 <= y and y <= lim:
                        locs.append((nx, y))
                else:
                    locs.append((nx, y))
            return locs if not x_only else [x[0] for x in locs]
        
    def get_reachable_manhattan(self, lim=20):
        locs = []
        for dx in range(-self.dist, self.dist + 1):
            for dy in range(-self.dist, self.dist + 1):
                if abs(dx) + abs(dy) <= self.dist:
                    nx, ny = self.loc[0] + dx, self.loc[1] + dy
                    if 0 <= nx and nx <= lim and 0 <= ny and ny <= lim:
                        locs.append((nx, ny))
        return locs

    def get_manhattan_ranges(self, lim=20):
        ranges = {}
        for dy in range(-self.dist, self.dist + 1):
            ny = self.loc[1] + dy
            if 0 <= ny and ny <= lim:
                offset = self.dist - abs(dy)
                start = (self.loc[0] + -offset)
                end = (self.loc[0] + offset)
                ranges[ny] = (max(start, 0), min(end, lim))
        return ranges


def get_sensors(data):
    lines = [parse_coord_line(l) for l in data]
    return [Sensor(x[0], x[1]) for x in lines]

def first_star(data, val=10):
    sensors = get_sensors(data)
    beacons = set([x.beacon for x in sensors])
    bad_locs = []
    for sensor in sensors:
        bad_locs.extend(sensor.reachable_on_y(val))
    return len(set([x for x in bad_locs if x not in beacons]))

# For every location, check each sensor, and find the gap
# For every y, check each sensor and find the gap
# For every sensor, find all points, jam them together, and find the gap (crashes)
# ?

def inefficient_second_star(data, lim=20):
    sensors = get_sensors(data)
    for y in range(0, lim + 1):
        bad_locs = []
        for sensor in sensors:
            bad_locs.extend(sensor.reachable_on_y(y, lim, x_only=True))
        if len(set(bad_locs)) <= lim:
            bad_locs = sorted(set(bad_locs))
            for i in range(1, len(bad_locs)):
                if bad_locs[i] != bad_locs[i - 1] + 1:
                    return 4000000 * (bad_locs[i] - 1) + y
            
def still_inefficient_second_star(data, lim=20):
    sensors = get_sensors(data)
    locs = []
    for s in sensors:
        print(s)
        locs.extend(s.get_reachable_manhattan(lim))
    locs = set(locs)
    rows = defaultdict(lambda: [])
    for loc in locs:
        rows[loc[0]].append(loc[1])
    for x, val in rows.items():
        if len(val) <= lim:
            val = sorted(val)
            for i in range(1, len(val)):
                if val[i] != val[i - 1] + 1:
                    return 4000000 * (x) + (val[i] - 1)

def collapse_ranges(range_set):
    range_set = sorted(range_set)
    while len(range_set) > 1:
        first = range_set[0]
        second = range_set[1]
        if first[0] <= second[0] and first[1] < second[1] and first[1] >= second[0] - 1:
            new_range = (first[0], second[1])
        elif first[0] <= second[0] and first[1] >= second[1]:
            new_range = (first[0], first[1])
        else:
            return first, second
        range_set = [new_range, *range_set[2:]]
    return range_set

def second_star(data, lim=20):
    sensors = get_sensors(data)
    ranges = defaultdict(lambda: [])
    for s in sensors:
        new_ranges = s.get_manhattan_ranges(lim)
        for k, v in new_ranges.items():
            ranges[k].append(v)
    for k, v in ranges.items():
        rng = collapse_ranges(v)
        if len(rng) > 1:
            x = rng[0][1] + 1
            return 4000000 * x + k

def solution(source):
    data = load_input(source)
    print("Day 15")
    print("First star:", str(first_star(data, 2000000)))
    print("Second star:", str(second_star(data, 4000000)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

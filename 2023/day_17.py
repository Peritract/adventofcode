import heapq

DIRS = {
    "N": (0, -1),
    "S": (0, 1),
    "W": (-1, 0),
    "E": (1, 0)
}

REVERSE_DIRS = {
    (0, -1): "N",
    (0, 1) : "S",
    (-1, 0): "W",
    (1, 0): "E"
}

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data


class Node:
    def __init__(self, x, y, heat_loss, width, height):
        self.x = x
        self.y = y
        self.loss = int(heat_loss)
        self.neighbours = self.get_neighbours(width, height)
        self.dist = 1000000 + (width - x) + (height - y)
        self.visited = False
        self.path_to = ""
    
    @property
    def loc(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return f"<{self.loc}: {self.loss}>"
    
    def get_neighbours(self, width, height):
        neighbours = {}
        for k, v in DIRS.items():
            nx, ny = self.x + v[0], self.y + v[1]
            if 0 <= nx < width and 0 <= ny < height:
                neighbours[k] = (nx, ny)
        return neighbours
    
    def get_allowed_neighbours(self, dir=None):
        return [v for k,v in self.neighbours.items() if k != v]
    
    def __lt__(self, other):
        return other.dist > self.dist
    
    def get_direction_of_entry(self, other):
        if other:
            nx, ny = self.loc[0] - other[0], self.loc[1] - other[1]
            return REVERSE_DIRS[(nx, ny)]

def construct_network(data):
    n = {}
    w = len(data[0])
    h = len(data)
    for y in range(h):
        for x in range(w):
            n[(x, y)] = Node(x, y, data[y][x], w, h)
    return n

def is_valid_path(path):
    if any([x in path for x in ["EEEE","WWWW","NNNN","SSSS"]]):
        return False
    return True

def first_star(data):
    network = construct_network(data)
    start = network[(0, 0)]
    end = (len(data[0]) - 1, len(data) - 1)
    start.dist = 0
    visited = set()
    possible = []
    heapq.heapify(possible)
    heapq.heappush(possible, start)
    last = None
    while len(possible):
        curr = heapq.heappop(possible)
        for n in curr.get_allowed_neighbours():
            n = network[n]
            path = curr.path_to + n.get_direction_of_entry(curr.loc)
            if is_valid_path(path) and n.loc not in visited:
                new_dist = curr.dist + n.loss
                if new_dist < n.dist:
                    n.dist = new_dist
                    n.path_to = path
                heapq.heappush(possible, n)
        visited.add(curr.loc)
        last = curr.loc
    print(network[end].path_to)
    return network[end].dist


def second_star(data):
    return "Not solved"


def solution(source):
    data = load_input(source)
    print("Day 17")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

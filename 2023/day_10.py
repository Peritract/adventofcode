REPLACEMENTS = {
    "." : ["...", "...", "..."],
    "-" : ["...", "XXX", "..."],
    "|" : [".X.", ".X.", ".X."],
    "7" : ["...", "XX.", ".X."],
    "J" : [".X.", "XX.", "..."],
    "L" : [".X.", ".XX", "..."],
    "F" : ["...", ".XX", ".X."]
}

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

class PipeSection:

    dirs = {
        "N": (0, -1),
        "S": (0, 1),
        "W": (-1, 0),
        "E": (1, 0)
    }
    connections = {
        "N": "S",
        "S": "N",
        "E": "W",
        "W": "E"
    }

    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
        self.is_start = True if char == "S" else False
        self.is_loop = True if self.is_start else False
        self.allowed_connections = self.get_allowed_connections()
        self.possible_neighbours = self.get_possible_neighbours()
        self.connections = None
        self.free = None


    @property
    def loc(self):
        return (self.x, self.y)

    def get_allowed_connections(self):
        if self.is_start:
            return ["N", "S", "E", "W"]
        elif self.char == ".":
            return []
        elif self.char == "|":
            return ["N", "S"]
        elif self.char == "-":
            return ["E", "W"]
        elif self.char == "L":
            return ["N", "E"]
        elif self.char == "J":
            return ["N", "W"]
        elif self.char == "7":
            return ["S", "W"]
        elif self.char == "F":
            return ["S", "E"]
        
    def get_possible_neighbours(self):
        neighbours = {}
        for d in self.allowed_connections:
            dl = PipeSection.dirs[d]
            n = (self.x + dl[0], self.y + dl[1])
            neighbours[d] = n
        return neighbours
    
    def big_rep(self):
        return REPLACEMENTS[self.char] if self.is_loop else REPLACEMENTS["."]
    
    def __repr__(self):
        return f"{self.loc}: {self.connections}"
    
    def get_valid_connections(self, nodes):
        connections = []
        for d, n in self.possible_neighbours.items():
            neighbour = nodes.get(n)
            if neighbour:
                if PipeSection.connections[d] in neighbour.allowed_connections:
                    connections.append(n)
        return connections
    
    def traverse(self, from_node):
        return [c for c in self.connections
                if c != from_node][0]
    
    def get_adjacent_cells(self, network):
        adj = []
        for dx, dy in PipeSection.dirs.values():
            poss = (self.x + dx, self.y + dy)
            if network.get(poss):
                adj.append(poss)
        return adj
    
    def get_direction(self, asker):
        nx, ny = asker
        if (self.x - nx) == 0:
            return "V"
        else:
            return "H"

    def allows_passage_from(self, asker):
        if not asker:
            return True
        if not self.is_loop:
            return True
        else:
            dir = self.get_direction(asker)
            if self.char == "-" and dir == "H":
                return True
            elif self.char in "|JLF7" and dir == "V":
                return True
            return False

    def can_reach_edge(self, width, height, network, asker=None, visited=None):

        if not self.allows_passage_from(asker):
            return False

        if not visited:
            visited = set()

        # Already known
        if self.free is not None:
            return self.free
        
        # On an edge
        elif self.x in (0, width - 1) or self.y in (0, height - 1):
            self.free = True # Edges are not enclosed
            return True
        
        # Check routes outwards
        else:
            # Get all the neighbours
            possibles = self.get_adjacent_cells(network)
            # Stop neighbours checking this cell again
            visited.add(self.loc)

            # For each neighbour
            for p in possibles:
                if p not in visited:
                    check = network[p].can_reach_edge(width, height,
                                                    network,
                                                    self.loc,
                                                    visited) # Include asker
                    visited.add(p)
                    if check:
                        self.free = True  # A free neighbour means free
                        return True
                
        # No route found
        return False


def build_big_grid(data, network):
    big_grid = []
    for y in range(len(data)):
        expansions = []
        for x in range(len(data[0])):
            expansions.append(network[(x, y)].big_rep())
        for i in range(3):
            big_grid.append(list("".join([g[i] for g in expansions])))
    return big_grid


def build_network(data):
    nodes = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            p = PipeSection(x, y, data[y][x])
            nodes[p.loc] = p
    for node in nodes.values():
        node.connections = node.get_valid_connections(nodes)
    return nodes


def identify_loop(network, start):
    start = network[start]
    start.is_start = True
    start.is_loop = True
    from_node = start.loc
    node = network[start.connections[0]]
    while not node.is_start:
        node.is_loop = True
        new_node = network[node.traverse(from_node)]
        from_node = node.loc
        node = new_node
    return network


def locate_start(data):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "S":
                return (x, y)

def identify_pipe(x, y, data):
    if data[y][x - 1] in "-FL":
        if data[y-1][x] in "|F7":
            return "J"
        elif data[y+1][x] in "|JL":
            return "7"
        else:
            return "-"
    if data[y - 1][x] in "|F7":
        if data[y][x-1] in "-FL":
            return "J"
        elif data[y][x+1] in "-7J":
            return "L"
        else:
            return "|"
    if data[y + 1][x] in "|JL":
        if data[y][x-1] in "-FL":
            return "7"
        if data[y][x+1] in "-7J":
            return "F"
        else:
            return "|"
        

def flood_fill(grid, x, y, nodes):
    grid[y][x] = " "
    for dx, dy in ((0,1), (0,-1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] not in "X ":
                nodes.append((nx, ny))


def flood_fill_grid(grid):
    nodes = []
    for y in range(len(grid)):
        for x in range(len(grid)):
            if x in (0, len(grid[0]) - 1) or y in (0, len(grid) - 1):
                nodes.append((x, y))
    while len(nodes) > 0:
        n = nodes.pop()
        flood_fill(grid, n[0], n[1], nodes)
    return grid


def shrink_grid(grid):
    small_grid = []
    for y in range(0, len(grid), 3):
        row = []
        for x in range(0, len(grid[0]), 3):
            segment = [grid[y + iy][x + ix] for iy in range(3) for ix in range(3)]
            row.append("X" if "X" in segment else segment[4])
        small_grid.append("".join(row))
    return small_grid

def first_star(data):
    network = build_network(data)
    start = [n for n in network.values() if n.is_start][0]
    from_node = start.loc
    node = network[start.connections[0]]
    steps = 0
    while not node.is_start:
        node.is_loop = True
        new_node = network[node.traverse(from_node)]
        from_node = node.loc
        node = new_node
        steps += 1
    return int((steps + 1) / 2)


def second_star(data):
    start = locate_start(data)
    start_pipe = identify_pipe(start[0], start[1], data)
    tmp = list(data[start[1]])
    tmp[start[0]] = start_pipe
    data[start[1]] = tmp
    network = build_network(data)
    network = identify_loop(network, start)
    
    big_grid = build_big_grid(data, network)

    flood_grid = flood_fill_grid(big_grid)

    small_grid = shrink_grid(flood_grid)
    
    # display_grid(small_grid)

    return "".join(small_grid).count(".")


def solution(source):
    data = load_input(source)
    print("Day 10")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

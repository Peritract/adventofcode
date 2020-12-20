# I needed some help with this one - I got lost in my head and went in the wrong direction for a while.

import re
from math import prod, sqrt
from collections import defaultdict

class Tile:
    
    def __init__(self, id, grid):
        self.id = id
        self.grid = grid
        self.unique_edges = None
        self.placed = False
    
    def __str__(self):
        return f'TILE {self.id}'
    
    @property
    def dir_edges(self):
        return {'U': self.grid[0],
                'D': "".join(reversed(self.grid[-1])),
                'L': "".join([x[0] for x in self.grid]),
                'R': "".join([x[-1] for x in self.grid])}
    
    @property
    def edges(self):
        return [x for x in self.dir_edges.values()]
    
    @property
    def edges_r(self):
        return ["".join(reversed(x)) for x in self.dir_edges.values()]
    
    @property
    def is_edge(self):
        if self.unique_edges and len(self.unique_edges) == 1:
            return True
        return False
    
    @property
    def is_corner(self):
        if self.unique_edges and len(self.unique_edges) == 2:
            return True
        return False
    
    def rotate(self, inplace=False):
        if inplace:
            self.grid = ["".join(list(reversed(x))) for x in zip(*self.grid)]
        else:
            return ["".join(list(reversed(x))) for x in zip(*self.grid)]
        
    def flip(self, inplace=False):
        if inplace:
            self.grid = list(reversed(self.grid))
        else:
            return list(reversed(self.grid))
        
    def display(self):
        print(f'TILE {self.id}')
        for x in self.grid:
            print(x)
        print('-' * len(self.grid))
        
    def find_unique_edges(self, edges):
        unique = []
        for edg in self.edges:
            if edges[edg] == 1:
                unique.append(edg)
        self.unique_edges = unique
        
    def orient_corner(self):
        if self.is_corner:
            check = sorted(self.unique_edges[:2]) == sorted([self.dir_edges['U'], self.dir_edges['L']])
            while not check:
                self.rotate(True)
                check = sorted(self.unique_edges[:2]) == sorted([self.dir_edges['U'], self.dir_edges['L']])
            
class Chart:
    
    def __init__(self, tiles):
        self.size = int(sqrt(len(tiles.values())))
        self.tiles = situate_tiles(tiles)
        self.grid = [[None for x in range(self.size)] for y in range(self.size)]
        self.corners = [x.id for x in self.tiles.values() if x.is_corner]
        
    @property
    def grid_complete(self):
        for y in self.grid:
            for x in y:
                if x == None:
                    return False
        return True
    
    def display(self):
        for y in self.grid:
            for x in y:
                print(x if x else None, end='\t')
            print('')
    
    def in_bounds(self, y, x):
        return 0 <= y < self.size and 0 <= x < self.size
    
    def in_sequence(self, y, x):
        if ((not self.in_bounds(y - 1, x)) or self.grid[y - 1][x]) and ((not self.in_bounds(y, x -1)) or self.grid[y][x - 1]):
            return True
        return False
    
    def place_tile(self, y, x):
        # If in-bounds and previous tiles have been placed and not already occupied
        if self.in_bounds(y, x) and self.in_sequence(y, x) and not self.grid[y][x]:
        
            # Get references to the previous tiles
            U = self.tiles[self.grid[y - 1][x]] if self.in_bounds(y - 1, x) else None
            L = self.tiles[self.grid[y][x - 1]] if self.in_bounds(y, x - 1) else None
            
            # Go with up first
            other = U if U else L
            
            # Roll through the tiles
            for tile in self.tiles.values():
                # Check if each tile is a valid placement here
                valid = False
                if not tile.placed:
                    if any([edg in other.edges for edg in tile.edges]):
                        valid = True
                    elif any([edg in other.edges for edg in tile.edges_r]):
                        valid = True
                        tile.flip(True)
                if valid:
                    turns = 0
                    while turns < 4:
                        tile.rotate(True)
                        if (not U or U.dir_edges['D'] == tile.dir_edges['U']) and (not L or L.dir_edges['R'] == tile.dir_edges['L']):
                            self.grid[y][x] = tile.id
                            tile.placed = True
                            return
                        turns += 1
                    
                    print('--------')
                    
                    return

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        data = [x.strip() for x in file.read().split("\n\n")]
    tiles = {}
    for x in data:
        lines = [y.strip() for y in x.split('\n')]
        t_id = int(re.findall('\d+',lines[0])[0])
        tile = Tile(t_id, lines[1:])
        tiles[t_id] = tile
    return tiles

def situate_tiles(tiles):
    edges = defaultdict(lambda: 0)
    for tile in tiles.values():
        for edge in tile.edges:
            edges[edge] += 1
            edges[''.join(reversed(edge))] += 1
    for tile in tiles.values():
        tile.find_unique_edges(edges)
    return tiles

def first_star(tiles):
    tiles = situate_tiles(tiles)
    corners = []
    for tile in tiles.values():
        if tile.is_corner:
            corners.append(tile.id)
    return prod(corners)
        
def second_star(tiles):
    tiles[1951].flip(True)
    chart = Chart(tiles)
    
    # Pick a starting corner
    start = tiles[chart.corners[0]]
    # Flip it to face into the grid
    start.orient_corner()
    # Place the tile in the top-left of the grid
    chart.grid[0][0] = start.id
    start.placed = True
    chart.place_tile(0, 1)
    chart.place_tile(1, 0)
    chart.place_tile(1, 1)
    chart.display()

def solution(source):
    data = load_input(source)
    print("Day 20")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

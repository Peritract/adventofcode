"""
I needed lots of help with this one - I solved the morning reasonably fast, but then had to rebuild it for part 2, and
in so doing, got myself completely turned around. I had to have someone talk me through their solution for part 1 before
I could rebuild mine again. After that, it went relatively quickly except for the eon spent trying to work out what was
wrong with my .flip (nothing was wrong - I had an error in my corner orientation). Finally I got the map working, but
kept on getting the wrong answer. I was not carefully handling multiple monsters on one line, or overlapping monsters; a
hint on Reddit let me know what to look for.
"""

import re
import regex
from math import prod, sqrt
from collections import defaultdict

class Tile:
    
    def __init__(self, id, grid):
        self.id = id
        self.grid = grid
        self.unique_edges = None
        self.placed = False
        self.size = len(grid)
    
    def __str__(self):
        return f'TILE {self.id}'
    
    @property
    def edges_d(self):
        return {'U': self.grid[0],
                'R': "".join([x[-1] for x in self.grid]),
                'D': self.grid[-1],
                'L': "".join([x[0] for x in self.grid])}
    
    @property
    def edges(self):
        return [x for x in self.edges_d.values()]
    
    @property
    def edges_r(self):
        return ["".join(reversed(x)) for x in self.edges_d.values()]
    
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
            for i in range(0, 3):
                if self.edges_d['U'] in self.unique_edges and self.edges_d['L'] in self.unique_edges:
                    return
                else:
                    self.rotate(True)
            self.flip(True)
            for i in range(0, 3):
                if self.edges_d['U'] in self.unique_edges and self.edges_d['L'] in self.unique_edges:
                    return
                else:
                    self.rotate(True)
                    
    def get_borderless_grid(self):
        return [x[1:-1] for x in self.grid[1:-1]]
    
    def count_hashes(self):
        return sum([x.count('#') for x in self.grid])
            
class Chart:
    
    def __init__(self, tiles):
        self.size = int(sqrt(len(tiles.values())))
        self.tiles = situate_tiles(tiles)
        self.grid = [[None for x in range(self.size)] for y in range(self.size)]
        self.corners = [x.id for x in self.tiles.values() if x.is_corner]
        self.tapestry = None
        self.monster = ['..................#.',
                        '#....##....##....###',
                        '.#..#..#..#..#..#...']
        
        self.fill_grid()
        self.stitch_tapestry()

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
                    for i in range(4):
                        if (not U or U.edges_d['D'] == tile.edges_d['U']) and (not L or L.edges_d['R'] == tile.edges_d['L']):    
                            tile.placed = True
                            self.grid[y][x] = tile.id
                            return
                        else:
                            tile.rotate(True)
                    tile.flip(True)
                    for i in range(4):
                        if (not U or U.edges_d['D'] == tile.edges_d['U']) and (not L or L.edges_d['R'] == tile.edges_d['L']):
                            tile.placed = True
                            self.grid[y][x] = tile.id
                            return
                        else:
                            tile.rotate(True)
    
    def fill_grid(self):
        # Pick a starting corner
        start = self.tiles[self.corners[0]]
        # Flip it to face into the grid
        start.orient_corner()
        # Place the tile in the top-left of the grid
        self.grid[0][0] = start.id
        start.placed = True

        while not self.grid_complete:
            for y in range(self.size):
                for x in range(self.size):
                    self.place_tile(y, x)
                    
    def stitch_tapestry(self):
        tapestry = []
        grid_size = len(list(self.tiles.values())[0].get_borderless_grid())
        for row in self.grid:
            for i in range(grid_size):
                line = []
                for col in row:
                    line.append(self.tiles[col].get_borderless_grid()[i])
                tapestry.append("".join(line))
        self.tapestry = Tile('TAPESTRY', tapestry)
            
    def scan_for_monsters(self):
        count = 0
        grid = self.tapestry.grid
        for i in range(self.tapestry.size - 2):
            matches = regex.finditer(self.monster[2], grid[i + 2], overlapped=True)
            for match in matches:
                if match:
                    span = match.span()
                    if re.match(self.monster[0], grid[i][span[0]:span[1]]) and re.match(self.monster[1], grid[i + 1][span[0]:span[1]]):
                        count += 1
        return count
    
    def monster_size(self):
        return sum([x.count('#') for x in self.monster])

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
    chart = Chart(tiles)
    for i in range(0, 4):
        monsters = chart.scan_for_monsters()
        if monsters > 0:
            print(f'FOUND {monsters} monsters')
            monstotal = monsters * chart.monster_size()
            print(chart.tapestry.count_hashes() - monstotal)
        chart.tapestry.rotate(True)
    chart.tapestry.flip(True)
    for i in range(0, 4):
        monsters = chart.scan_for_monsters()
        if monsters > 0:
            monstotal = monsters * chart.monster_size()
            print(chart.tapestry.count_hashes() - monstotal)
        chart.tapestry.rotate(True)
    
def solution(source):
    data = load_input(source)
    print("Day 20")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

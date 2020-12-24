from collections import defaultdict

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [x.strip() for x in file.readlines()]

def parse_line(line):
    cmds = []
    index = 0
    while index < len(line):
        if line[index] in ('w', 'e'):
            cmds.append(line[index])
            index += 1
        else:
            cmds.append(line[index:index+2])
            index += 2
    return cmds

dirs = {
    'e' : (1, -1, 0),
    'w' : (-1, 1, 0),
    'nw' : (0, 1, -1),
    'ne' : (1, 0, -1),
    'sw' : (-1, 0, 1),
    'se' : (0, -1, 1)
}

def add_step(t, step):
    for i in range(len(t)):
        t[i] += step[i]
    return t

def get_tile_location(cmds):
    
    # E-W, NE-SW, NW-SE
    tile = [0, 0, 0]
    
    for x in cmds:
        tile = add_step(tile.copy(), dirs[x])

    return tile
        
def count_black(tiles):
    return sum([1 for x in tiles.values() if x == 'b'])

def lay_floor(data):
    instructions = [parse_line(x) for x in data]
    tiles = defaultdict(lambda: 'w')
    for ins in instructions:
        tile = tuple(get_tile_location(ins))
        if tiles[tile] == 'w':
            tiles[tile] = 'b'
        else:
            tiles[tile] = 'w'
    return tiles

def first_star(data):
    return count_black(lay_floor(data))

def count_neighbours(tile, tiles):
    count = 0
    loc = list(tile)
    for k, v in dirs.items():
        neighbour = add_step(loc.copy(), v)
        if tiles[tuple(neighbour)] == 'b':
            count += 1
    return count

def count_conservative_neighbours(tile, tiles):
    count = 0
    loc = list(tile)
    for dir in dirs.values():
        neighbour = tuple(add_step(loc.copy(), dir))
        if neighbour in tiles and tiles[neighbour] == 'b':
            count += 1
    return count
        
def second_star(data, turns=100):
    tiles = lay_floor(data)
    for x in range(turns):
        for tile in list(tiles.keys()):
            count_neighbours(tile, tiles)
    tiles = dict(tiles)
    for i in range(turns):
        new_tiles = {}
        for tile in tiles.keys():
            n = count_conservative_neighbours(tile, tiles)
            colour = tiles[tile]
            if tiles[tile] == 'w' and n == 2:
                colour = 'b'
            elif (tiles[tile] == 'b' and n == 0) or (tiles[tile] == 'b' and n > 2):
                colour = 'w'
            new_tiles[tile] = colour

        tiles = new_tiles
    return count_black(tiles)
    
def solution(source):
    data = load_input(source)
    print("Day 24")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

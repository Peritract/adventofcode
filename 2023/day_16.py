DIRS = {
    "N": (0, -1),
    "S": (0, 1),
    "W": (-1, 0),
    "E": (1, 0)
}

MIRROR_B = {
    "E": "S",
    "S": "E",
    "N": "W",
    "W": "N"
}

MIRROR_F = {
    "E": "N",
    "S": "W",
    "N": "E",
    "W": "S"
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

def display_complex_grid(grid, lookup):
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[1])):
            row += "#" if (x, y) in lookup else grid[y][x]
        print(row)
    print("")

def in_bounds(beam, w, h):
    if 0 <= beam[0] < w and 0 <= beam[1] < h:
        return True
    return False

def progress(beam):
    dx, dy = DIRS[beam[2]]
    return (beam[0] + dx, beam[1] + dy, beam[2])

def count_energised(grid, starting_point):
    width = len(grid[0])
    height = len(grid[1])
    beams = [starting_point]
    change = True
    energised = set()
    while len(beams) > 0 and change:
        change = False
        for i, b in enumerate(beams):
            if in_bounds(b, width, height):
                if (b) not in energised:
                    change = True
                    energised.add(b)
                cell = grid[b[1]][b[0]]
                if cell == "." or (cell == "-" and b[2] in "EW") or (cell == "|" and b[2] in "NS"):
                    beams[i] = progress(b)
                elif cell in "\\":
                    beams[i] = progress((b[0], b[1], MIRROR_B[b[2]]))
                elif cell == "/":
                    beams[i] = progress((b[0], b[1], MIRROR_F[b[2]]))
                elif cell == "|":
                    beams[i] = progress((b[0], b[1], "N"))
                    beams.append(progress((b[0], b[1], "S")))
                elif cell == "-":
                    beams[i] = progress((b[0], b[1], "W"))
                    beams.append(progress((b[0], b[1], "E")))
        beams = list(filter(lambda x: in_bounds(x, width, height) and x not in energised, beams))
    return len(set((e[0], e[1]) for e in energised))
    
def generate_all_starting_locs(width, height):
    locs = []
    for y in range(height):
        locs.append((0, y, "E"))
        locs.append((width - 1, y, "W"))
    for x in range(width):
        locs.append((x, 0, "S"))
        locs.append((x, height - 1, "N"))
    return locs

def first_star(data):
    return count_energised(data, (0, 0, "E"))


def second_star(data):
    locs = generate_all_starting_locs(len(data[0]), len(data))
    return max(count_energised(data, l) for l in locs)


def solution(source):
    data = load_input(source)
    print("Day 16")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

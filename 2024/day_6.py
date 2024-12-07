def load_input(source):
    with open(source) as f:
        data = [list(l.strip()) for l in f.readlines()]
    return data

def get_char_at(grid, x, y):
    return grid[y][x]

def get_locs_of(grid, char):
    locs = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == char:
                locs.append((x, y))
    return locs

def in_bounds(grid, x, y):
    return (0 <= x < len(grid[0])) and (0 <= y < len(grid))

def first_star(grid):
    return len(get_standard_visited(grid))

def get_standard_visited(grid):
    start = get_locs_of(grid, "^")[0]
    obs = get_locs_of(grid, "#")
    visited = [start]
    curr = start
    dirs = {
        "N": (0, -1),
        "W": (-1, 0),
        "S": (0, 1),
        "E": (1, 0)
    }
    dir = "N"
    while in_bounds(grid, *curr):
        dest = curr[0] + dirs[dir][0], curr[1] + dirs[dir][1]
        if dest not in obs:
            visited.append(dest)
            curr = dest
        else:
            if dir == "N":
                dir = "E"
            elif dir == "E":
                dir = "S"
            elif dir == "S":
                dir = "W"
            else:
                dir = "N"

    return set(visited[:-1])

def gets_caught_in_loop(grid):
    start = get_locs_of(grid, "^")[0]
    obs = get_locs_of(grid, "#")
    curr = start
    dirs = {
        "N": (0, -1),
        "W": (-1, 0),
        "S": (0, 1),
        "E": (1, 0)
    }
    dir = "N"
    visited = [(start, dir)]
    while in_bounds(grid, *curr):
        dest = curr[0] + dirs[dir][0], curr[1] + dirs[dir][1]
        if dest not in obs:
            if (dest, dir) in visited:
                return True
            visited.append((dest, dir))
            curr = dest
        else:
            if dir == "N":
                dir = "E"
            elif dir == "E":
                dir = "S"
            elif dir == "S":
                dir = "W"
            else:
                dir = "N"
    return False

def second_star(grid):
    loops = 0
    original_visits = get_standard_visited(grid)
    for x, y in original_visits:
        if get_char_at(grid, x, y) == ".":
            print(x, y)
            poss_grid = [[x for x in r] for r in grid]
            poss_grid[y][x] = "#"
            loops += gets_caught_in_loop(poss_grid)
    return loops
    
def solution(source):
    data = load_input(source)
    print("Day 6")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

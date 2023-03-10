def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
        data = [[e for e in r] for r in data]
    return data

def poll_neighbours(grid, y, x):
    count = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            ny, nx = y + dy, x + dx
            if (ny == y and nx == x) or ny < 0 or nx < 0 or ny >= len(grid) or nx >= len(grid[0]):
                continue
            if grid[ny][nx] == "#":
                count += 1
    return count


def display_grid(grid):
    for row in grid:
        print("".join(row))
    print("-" * len(grid[0]))


def first_star(data):
    grid = data
    for step in range(100):
        new_grid = [[" " for x in range(len(grid[0]))] for y in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                state = grid[y][x]
                n_on = poll_neighbours(grid, y, x)
                if state == "#":
                    new_grid[y][x] = "#" if n_on in (2, 3) else "."
                else:
                    new_grid[y][x] = "#" if n_on == 3 else "."
        grid = new_grid
    count = 0
    for y in grid:
        for x in y:
            count += 1 if x == "#" else 0
    return count

def second_star(data):
    grid = data
    grid[0][0] = "#"
    grid[len(grid) - 1][0] = "#"
    grid[0][len(grid[0]) -1] = "#"
    grid[len(grid) - 1][len(grid[0]) - 1] = "#"
    display_grid(grid)
    for step in range(100):
        new_grid = [[" " for x in range(len(grid[0]))] for y in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                state = grid[y][x]
                n_on = poll_neighbours(grid, y, x)
                if (y, x) in ((0,0), (len(grid) - 1, 0), (0, len(grid[0]) - 1), (len(grid) - 1, len(grid[0]) - 1)):
                    new_grid[y][x] = "#"
                elif state == "#":
                    new_grid[y][x] = "#" if n_on in (2, 3) else "."
                else:
                    new_grid[y][x] = "#" if n_on == 3 else "."
        grid = new_grid
        display_grid(grid)
    count = 0
    for y in grid:
        for x in y:
            count += 1 if x == "#" else 0
    return count


def solution(source):
    data = load_input(source)
    print("Day 18")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

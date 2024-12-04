def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data

def is_xmas_in_dir(start, grid, dir):
    letters = ""
    cx, cy = start
    for i in range(3):
        nx, ny = cx + dir[0], cy + dir[1]
        if (0 <= nx < len(grid[0])) and (0 <= ny < len(grid)):
            letters += grid[ny][nx]
        cx, cy = nx, ny
    return letters == "MAS"

def is_x_mas(start, grid):
    letters = ""
    for dx, dy in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        nx, ny = start[0] + dx, start[1] + dy
        if (0 <= nx < len(grid[0])) and (0 <= ny < len(grid)):
            letters += grid[ny][nx]
    return letters in ("MMSS", "SSMM", "MSMS", "SMSM")


def first_star(data):
    starts = []
    xmas_count = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "X":
                starts.append((x, y))
    for x in starts:
        for d in ((0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)):
            xmas_count += is_xmas_in_dir(x, data, d)
    return xmas_count


def second_star(data):
    starts = []
    x_mas_count = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "A":
                starts.append((x, y))
    for x in starts:
        x_mas_count += is_x_mas(x, data)
    return x_mas_count
    
def solution(source):
    data = load_input(source)
    print("Day 4")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("finput.txt")

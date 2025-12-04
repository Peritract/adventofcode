import re

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    
def preprocess_data(data):
    return [list(x) for x in data]

def is_accessible(x, y, grid):
    filled = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy
            if (0 <= nx < len(grid[0])) and (0 <= ny < len(grid)) and not (dx == 0 and dy ==0):
                filled += grid[ny][nx] == "@"
    return filled < 4

def first_star(data):
    print(data)
    count = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "@":
                count += is_accessible(x, y, data)
    return count

def second_star(data):
    count = 0
    check_again = True
    while check_again:
        check_again = False
        for y in range(len(data)):
            for x in range(len(data[0])):
                if data[y][x] == "@":
                    if is_accessible(x, y, data):
                        count += 1
                        data[y][x] = '.'
                        check_again = True
    return count

def solution(source):
    data = preprocess_data(load_input(source))
    print("Day 4")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

from os import system
from time import sleep

def load_input(filename):
  with open(filename) as f_obj:
    return [x.strip() for x in f_obj.readlines()]

def get_vals(data):
    clock = 0
    reg = 1
    step = 0
    vals = [1]
    for inc in data:
        if inc == 'noop':
            clock += 1
            step += 1
            vals.append(reg)
        else:
            val = int(inc.split(" ")[1])
            clock += 2
            step += 2
            vals.extend([reg, reg + val])
            reg = reg + val
    return vals


def first_star(data):
    vals = get_vals(data)
    return sum([vals[x - 1] * x for x in range(20, 221, 40)])

def display_screen(grid):
    for row in grid:
        print("".join(row))

def second_star(data):
    grid = [["." for x in range(40)] for y in range(6)]
    vals = get_vals(data)
    for i in range(240):
        system("clear")
        y = i // 40
        x = i % 40
        val_x = vals[i] % 40
        rng = (val_x - 1 if val_x - 1 > -1 else 39, val_x, val_x + 1 if val_x + 1 < 40 else 0)
        if x in rng:
            grid[y][x] = '#'
        display_screen(grid)
        sleep(0.02)

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

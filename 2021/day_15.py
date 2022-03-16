def load_input(filename):
  with open(filename) as f_obj:
    return [x.strip() for x in f_obj.readlines()]

def create_grid(data):
  grid = []
  for y in data:
    grid.append([int(x) for x in y])
  return grid

def display_grid(grid):

  for y in grid:
    print("".join([str(x) for x in y]))
  print("---")
  

def get_valid_neighbours(x, y, w, h, valid):
  neighbours = []
  for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    n = (x + d[0], y + d[1])
    if n[0] >= 0 and n[1] >= 0 and n[0] < w and n[1] < h and n in valid:
      neighbours.append(n)
  return neighbours

def get_min_coords(dists, valid):
  min_coords = valid[0]
  min = dists[min_coords[1]][min_coords[0]]

  for val in valid:
    d = dists[val[1]][val[0]]
    if d != -1:
      if min == -1 or d < min:
        min_coords = val
        min = d
      
  return min_coords

def get_route_cost(grid):
  width = len(grid[0])
  height = len(grid)

  dists = [[-1 for x in range(width)] for y in range(height)]
  dists[0][0] = 0
  unvisited = []
  for y in range(height):
    for x in range(width):
      unvisited.append((x, y))

  while len(unvisited) > 0:
    curr = get_min_coords(dists, unvisited)
    if curr == (width, height):
      return dists[height - 1][width - 1]
    curr_dist = dists[curr[1]][curr[0]]
    unvisited.remove(curr)

    
    for n in get_valid_neighbours(curr[0], curr[1],
                                  width, height, unvisited):
      d = grid[n[1]][n[0]]
                                    
      if d + curr_dist < dists[n[1]][n[0]] or dists[n[1]][n[0]] < 0:
        dists[n[1]][n[0]] = d + curr_dist

  return dists[height - 1][width - 1]

def first_star(data):
  grid = create_grid(data)
  
  return get_route_cost(grid)

def boost_grid(grid, tot):
  new_grid = [[x for x in y] for y in grid]
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      curr = grid[y][x]
      for i in range(tot):
        if curr == 9:
          curr = 1
        else:
          curr += 1
      new_grid[y][x] = curr

  return new_grid      

def expand_grid(grid):
  width = len(grid[0])
  height = len(grid)

  expanded_grid = [["x" for x in range(width * 5)] for y in range(height * 5)]

  off_y = 0
  off_x = 0

  for i in range(5):
    for j in range(5):
      b_grid = boost_grid(grid, i+j)
      for ex_y in range(off_y, off_y + height):
        for ex_x in range(off_x, off_x + width):
          expanded_grid[ex_y][ex_x] = b_grid[ex_y - off_y][ex_x - off_x]
      off_x += width
    off_x = 0
    off_y += height

  
  return expanded_grid

def second_star(data):
  grid = create_grid(data)
  expanded_grid = expand_grid(grid)
  
  return get_route_cost(expanded_grid)

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

def load_input(filename):
  with open(filename) as f_obj:
    return [(x.strip().split(" ")[0], int(x.strip().split(" ")[1])) for x in f_obj.readlines()]

def get_new_head_position(h, dir):
    return [h[0] + dir[0], h[1] + dir[1]]

def is_touching(h, t):
    # if abs(diff) should also work
    if t[0] in (h[0] -1, h[0], h[0] + 1) and t[1] in (h[1] -1, h[1], h[1] + 1):
        return True
    return False

def get_new_tail_position(t, h):
    n_x = 1 if h[0] - t[0] > 0 else - 1 if h[0] - t[0] < 0 else 0
    n_y = 1 if h[1] - t[1] > 0 else - 1 if h[1] - t[1] < 0 else 0

    return [t[0] + n_x, t[1] + n_y]

def first_star(data):
    dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
    h = [0,0]
    t = [0, 0]
    seen = [(0, 0)]
    for line in data:
        for step in range(line[1]):
            h = get_new_head_position(h, dirs[line[0]])
            if not is_touching(h, t):
                t = get_new_tail_position(t, h)
                seen.append((t[0], t[1]))
    return len(set(seen))

def second_star(data):
    dirs = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
    knots = [[0, 0] for x in range(10)]
    seen = [(0, 0)]
    for line in data:
        for step in range(line[1]):
            knots[0] = get_new_head_position(knots[0], dirs[line[0]])
            for i in range(1, 10):
                if not is_touching(knots[i - 1], knots[i]):
                    knots[i] = get_new_tail_position(knots[i], knots[i - 1])
                    if i == 9:
                        seen.append((knots[i][0], knots[i][1]))
    return len(set(seen))

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

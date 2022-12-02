def load_input(filename):
  with open(filename) as f_obj:
    return [x.strip().split() for x in f_obj.readlines()]

def first_star(data):
    score = 0
    p = {'A': 1, 'B': 2, 'C': 3}
    m = { 'X' : 'A', 'Y': 'B', 'Z': 'C'}
    data = [(x[0], m[x[1]]) for x in data]
    for g in data:
        score += p[g[1]]
        if g[0] == g[1]:
            score += 3
        elif g in [('A', 'B'), ('B', 'C'), ('C', 'A')]:
            score += 6
        else:
            score += 0
    return score

def second_star(data):
    score = 0
    p = {'A': 1, 'B': 2, 'C': 3}
    for g in data:
        if g[1] == 'Y':
            score += 3
            score += p[g[0]]
        elif g[1] == 'Z':
            score += 6
            score += p[g[0]] + 1 if g[0] != 'C' else 1
        else:
            score += 0
            score += p[g[0]] - 1 if g[0] != 'A' else 3

    return score

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

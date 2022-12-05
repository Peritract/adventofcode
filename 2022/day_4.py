def load_input(filename):
  with open(filename) as f_obj:
    return [[[int(z) for z in y.split('-')] for y in x.strip().split(',')] for x in f_obj.readlines()]

def first_star(data):
    count = 0
    for pair in data:
        l_a = list(range(pair[0][0], pair[0][1] + 1))
        l_b = list(range(pair[1][0], pair[1][1] + 1))
        if all([x in l_b for x in l_a]) or all([x in l_a for x in l_b]):
            count += 1
    return count

def second_star(data):
    count = 0
    for pair in data:
        l_a = list(range(pair[0][0], pair[0][1] + 1))
        l_b = list(range(pair[1][0], pair[1][1] + 1))
        if any([x in l_b for x in l_a]) or any([x in l_a for x in l_b]):
            count += 1
    return count

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

def load_input(filename):
  with open(filename) as f_obj:
    return [x.strip() for x in f_obj.readlines()]

def first_star(data):
    score = 0
    for row in data:
        h = int(len(row) / 2)
        (a, b) = row[:h], row[h:]
        ans = list(filter(lambda x: x in b, a))[0]
        if ans.lower() == ans:
            score += ord(ans) - 96
        else:
            score += ord(ans) - 38
    return score

def second_star(data):
    score = 0
    for i in range(0, len(data), 3):
        ans = list(filter(lambda x: x in data[i] and x in data[i + 1], data[i + 2]))[0]
        if ans.lower() == ans:
            score += ord(ans) - 96
        else:
            score += ord(ans) - 38
    return score

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

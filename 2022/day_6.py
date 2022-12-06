def load_input(filename):
  with open(filename) as f_obj:
    return f_obj.read().strip()

def first_star(data):
    for i in range(4, len(data) + 1):
        if len(set(data[i-4:i])) == 4:
            return i

def second_star(data):
    for i in range(14, len(data) + 1):
        if len(set(data[i-14:i])) == 14:
            return i

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

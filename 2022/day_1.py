def load_input(filename):
  with open(filename) as f_obj:
    return [x.strip() for x in f_obj.readlines()]

def first_star(data):
    elves = []
    elf = 0
    for x in data:
        if x == '':
            elves.append(elf)
            elf = 0
        else:
            elf += int(x)

    return max(elves)

def second_star(data):
    elves = []
    elf = 0
    for x in data:
        if x == '':
            elves.append(elf)
            elf = 0
        else:
            elf += int(x)

    return sum(sorted(elves)[-3:])

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(data))
  print("Second star:", second_star(data))

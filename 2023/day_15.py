import re

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    
def hash(string):
    val = 0
    for c in string:
        val += ord(c)
        val = val * 17
        val = val % 256
    return val


def first_star(data):
    tot = 0
    for r in data.split(","):
        n = hash(r)
        tot += n
    return tot


def insert_lenses(instructions, boxes):
    for r in instructions:
        m = re.search(r"(.+?)([=-])(\d+)?", r)
        label, op, val = m.group(1), m.group(2), m.group(3)
        b = boxes[hash(label)]
        if op == "-":
            if label in b:
                del b[label]
        else:
            b[label] = int(val)
    return boxes

def get_lens_power(boxes):
    total = 0 
    for i in range(len(boxes)):
        for j, (k, v) in enumerate(boxes[i].items()):
            total += (i + 1) * (j + 1) * v
    return total

def second_star(data):
    instructions = data.split(",")
    boxes = [{} for x in range(256)]
    insert_lenses(instructions, boxes)
    return get_lens_power(boxes)


def solution(source):
    data = load_input(source)
    print("Day 15")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

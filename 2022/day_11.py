from copy import deepcopy
import re
from operator import add, mul, truediv, sub

def load_input(filename):
  with open(filename) as f_obj:
    return [parse_monkey(x.strip().split("\n")) for x in f_obj.read().split("\n\n")]

def parse_monkey(data):
    id = int(data[0][7])
    data = [re.split('[:,]\s', x.strip())[1:] for x in data[1:]]
    op = data[1][0].split(" ")[-2:]
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    return {
        'id': id,
        'items': [int(x) for x in data[0]],
        'op': lambda x: ops[op[0]](x, int(op[1] if op[1] != 'old' else x)),
        'test': lambda x: x % int(data[2][0].split(' ')[-1]) == 0,
        True: int(data[3][0][-1]),
        False: int(data[4][0][-1]),
        "seen": 0
    }

def first_star(data):
    for i in range(20):
        for m in range(len(data)):
            curr = data[m]
            count = len(curr['items'])
            for i in range(count):
                item = curr['items'].pop(0)
                item = curr['op'](item) // 3
                target = curr[curr['test'](item)]
                data[target]['items'].append(item)
                curr['seen'] += 1
    return mul(*sorted([x['seen'] for x in data])[-2:])

def second_star(data):
    pass

if __name__ == "__main__":
  data = load_input("input.txt")
  print("First star:", first_star(deepcopy(data)))
  print("Second star:", second_star(data))

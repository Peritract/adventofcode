from functools import reduce
from operator import mul
import re

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data


def parse_input(data):
    return {
        't': [int(x) for x in data[0].split()[1:]],
        'd': [int(x) for x in data[1].split()[1:]]
    }


def parse_unkerned_input(data):
    return (int("".join(re.findall("\d+", data[0]))),
            int("".join(re.findall("\d+", data[1]))))


def first_star(data):
    data = parse_input(data)
    win_counts = []
    for r in range(len(data['t'])):
        t, d = data['t'][r], data['d'][r]
        dsts = [hc for hc in range(t) if ((t - hc) * hc) > d]
        win_counts.append(len(dsts))
    return reduce(mul, win_counts, 1)


def second_star(data):
    t, d = parse_unkerned_input(data)
    dsts = [hc for hc in range(t) if ((t - hc) * hc) > d]
    return len(dsts)


def solution(source):
    data = load_input(source)
    print("Day 6")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

import re
from functools import reduce
from operator import mul

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    

def parse_games(data):
    data = [(int(re.search("\d+", g).group(0)),
             [{d.split()[1]: int(d.split()[0])
              for d in r.split(", ")}
             for r in 
             g.split(": ")[1].split(";")])
            for g in data]

    return data


def find_min_vals(a, b):
    return {'red': max(a.get("red", 0), b.get("red", 0)),
            'blue': max(a.get("blue", 0), b.get("blue", 0)),
            'green': max(a.get("green", 0), b.get("green", 0))}


def first_star(data):
    totals = {"red": 12, 'green': 13, 'blue': 14}
    valid_count = 0
    for g in data:
        print(g)
        poss = True
        for r in g[1]:
            for k in totals.keys():
                if k in r and r[k] > totals[k]:
                    poss = False
        valid_count += g[0] if poss else 0
    return valid_count


def second_star(data):
    tot = 0
    for g in data:
        min_vals = reduce(find_min_vals, g[1][1:], g[1][0]).values()
        tot += reduce(mul, min_vals, 1)
    return tot



def solution(source):
    data = parse_games(load_input(source))
    print("Day 2")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

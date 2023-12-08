import re

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data

def parse_network(data):
    network = {}
    for node in data:
        chunks = re.search("(\w{3}) = \((\w{3}), (\w{3})\)", node)
        network[chunks.group(1)] = (chunks.group(2), chunks.group(3))
    return network

def first_star(data):
    instructions = data[0]
    network = parse_network(data[2:])
    steps = 0
    loc = "AAA"
    while loc != "ZZZ":
        cmd = instructions[(steps) % len(instructions)]
        loc = network[loc][0 if cmd == "L" else 1]
        steps += 1
    return steps


def second_star(data):
    instructions = data[0]
    network = parse_network(data[2:])
    steps = 0
    locs = [k for k in network.keys() if k.endswith("A")]
    periods = [0 for i in range(len(locs))]
    
    while not all(periods):
        cmd = instructions[(steps) % len(instructions)]
        locs = [network[l][0 if cmd == "L" else 1] for l in locs]
        steps += 1
        for i in range(len(locs)):
            if locs[i].endswith("Z") and not periods[i]:
                periods[i] = steps
    periods = sorted(periods)

    val = periods[0]
    increment = periods[0]
    for i in range(len(periods) - 1):
        while val % periods[i + 1] != 0:
            val += increment
        increment = val
    return val
    return periods

def solution(source):
    data = load_input(source)
    print("Day 8")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

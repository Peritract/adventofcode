import re

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.read().split("\n\n")]
    if len(data) == 1:
        data = data[0]
    return data


def extract_details(data):
    details = {}
    for chunk in data:
        label = re.search("^([\w-]+)", chunk).group()
        if label == "seeds":
            details[label] = [int(x) for x in chunk.split(": ")[1].split()]
        else:
            ranges = {
                    "src": [],
                    "dst": []
                }
            for row in chunk.split(":\n")[1].split("\n"):
                row = [int(x) for x in row.split()]
                ranges["dst"].append((row[0], row[0] + row[2] -1))
                ranges["src"].append((row[1], row[1] + row[2] -1))
            details[label] = ranges
    return details


def find_qual_number(start, qual_dict):
    for i, rng in enumerate(qual_dict["src"]):
        if rng[0] <= start <= rng[1]:
            dst = qual_dict["dst"][i]
            return dst[0] + (start - rng[0])
            return(start, rng, )
    return start
    

def first_star(data):
    stages = list(data.keys())[1:]
    minimal = None
    for s in data["seeds"]:
        for stage in stages:
            s = find_qual_number(s, data[stage])
        if not minimal or s < minimal:
            minimal = s
    return minimal


def second_star(data):
    stages = list(data.keys())[1:]
    minimal = None
    seeds = []
    for i in range(0, len(data["seeds"]), 2):
        start = data["seeds"][i]
        end = data["seeds"][i] + data["seeds"][i + 1]
        seeds.extend([x for x in range(start, end)])
    print(len(seeds))
    for s in seeds:
        for stage in stages:
            s = find_qual_number(s, data[stage])
        if not minimal or s < minimal:
            minimal = s
    return minimal


def solution(source):
    data = extract_details(load_input(source))
    print("Day 5")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

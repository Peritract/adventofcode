import re

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data


def parse_input(data):
    return map(lambda x: (x[0], [int(y) for y in x[1].split(",")]), [r.split(" ")
        for r in data
    ])

CACHE = {
}

def generate_possibilities(row):
    if row in CACHE:
        return CACHE[row]
    options = []
    next_err = row.find("?")
    if next_err == -1:
        CACHE[row] = [row]
        return [row]
    safe = row[:next_err]
    ongoing_options = generate_possibilities(row[next_err + 1:])
    for o in ongoing_options:
        options.append(safe + "#" + o)
        options.append(safe + "." + o)
    CACHE[row] = options
    return options


def validate_possibility(row, check):
    p_err = [x for x in re.split("\.{1,}", row) if x]
    return check == p_err

def unfold(row):
    segments = []
    checks = []
    for i in range(5):
        segments.append(row[0])
        checks.extend(row[1])
    string = "?".join(segments)
    return (string, checks)

def first_star(data):
    data = parse_input(data)
    tot = 0
    for r in list(data):
        poss = generate_possibilities(r[0])
        c_err = ["#" * i for i in r[1]]
        tot += sum([validate_possibility(p, c_err) for p in poss])

    return tot


def second_star(data):
    data = parse_input(data)
    for r in list(data)[:1]:
        remaining = len(r[0]) - sum(r[1])
        print(remaining)
        print(r[0], ".".join(["#" * i for i in r[1]]))


def solution(source):
    data = load_input(source)
    print("Day 12")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

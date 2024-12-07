def load_input(source):
    with open(source) as f:
        data = [l.strip() for l in f.readlines()]
    return data

def parse_input(data):
    eqs = []
    for r in data:
        val, inps = r.split(': ')
        eqs.append((int(val), [int(i) for i in inps.split()]))
    return eqs

def is_valid(val, inps, concat=False):
    chunks = [inps[0]]
    for i in inps[1:]:
        n_chunks = []
        for c in chunks:
            n_chunks.append(c + i)
            n_chunks.append(c * i)
            if concat:
                n_chunks.append(int(str(c) + str(i)))
        chunks = n_chunks
    if val in chunks:
        return True
    return False


def first_star(data):
    tot = 0
    for r in data:
        if is_valid(r[0], r[1]):
            tot += r[0]
    return tot

def second_star(data):
    tot = 0
    for r in data:
        if is_valid(r[0], r[1], concat=True):
            tot += r[0]
    return tot


def solution(source):
    data = parse_input(load_input(source))
    print("Day 7")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

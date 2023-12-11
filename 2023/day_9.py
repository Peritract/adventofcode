def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data

def parse_input(data):
    return [[int(x) for x in r.split()] for r in data]

def get_sequence_diffs(seq):
    return [seq[i] - seq[i-1] for i in range(1, len(seq))]

def get_next_term(seq):
    diffs = get_sequence_diffs(seq)
    if len(set(diffs)) == 1 and diffs[0] == 0:
        return seq[-1]
    else:
        return seq[-1] + get_next_term(diffs)
    
def get_previous_term(seq):
    diffs = get_sequence_diffs(seq)
    if len(set(diffs)) == 1 and diffs[0] == 0:
        return seq[0]
    else:
        return (seq[0] - get_previous_term(diffs))

def first_star(data):
    seqs = parse_input(data)
    return sum(get_next_term(s) for s in seqs)


def second_star(data):
    seqs = parse_input(data)
    return sum(get_previous_term(s) for s in seqs)


def solution(source):
    data = load_input(source)
    print("Day 9")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data

def parse_lists(data):
    a, b = [], []
    for x in data:
        nums = [int(n) for n in x.split()]
        a.append(nums[0])
        b.append(nums[1])

    return [a, b]

def first_star(data):
    data[0], data[1] = sorted(data[0]), sorted(data[1])
    return sum([abs(data[0][x] - data[1][x]) for x in range(len(data[0]))])


def second_star(data):
    tot = 0
    for v in data[0]:
        tot += v * data[1].count(v)
    return tot

def solution(source):
    data = parse_lists(load_input(source))
    print("Day 1")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

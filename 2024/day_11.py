from collections import defaultdict

def load_input(source):
    with open(source) as f:
        data = [int(x) for x in f.read().split()]
    return data

def evolve(val):
    if val == 0:
        return 1
    elif len(str(val)) % 2 == 0:
        sval = str(val)
        nums = int(sval[:len(sval)//2]), int(sval[len(sval)//2:])
        return nums
    else:
        return val * 2024

def first_star(data):
    stones = data
    for i in range(25):
        nstones = []
        for s in stones:
            v = evolve(s)
            if isinstance(v, tuple):
                nstones.extend(v)
            else:
                nstones.append(v)
        stones = nstones
    return len(stones)

def second_star(data):
    stones = defaultdict(lambda: 0)
    for s in data:
        stones[s] += 1
    for i in range(75):
        n_stones = defaultdict(lambda: 0)
        for k in stones:
            v = evolve(k)
            if isinstance(v, tuple):
                n_stones[v[0]] += stones[k]
                n_stones[v[1]] += stones[k]
            else:
                n_stones[v] += stones[k]
        stones = n_stones
    return sum(v for v in stones.values())

def solution(source):
    data = load_input(source)
    print("Day 11")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

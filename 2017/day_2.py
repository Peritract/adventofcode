def load_input(source):
    with open(source) as f:
        data = [[int(v) for v in x.strip().split()]
                for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    
def get_divisor_difference(row: list[int]) -> int:

    for i in range(len(row)):
        for j in range(i+1, len(row)):
            div = row[i] / row[j]
            if  div == int(div):
                return int(div)


def first_star(data):
    return sum([max(x) - min(x) for x in data])


def second_star(data):
    return sum([get_divisor_difference(sorted(r, reverse=True))
                for r in data])


def solution(source):
    data = load_input(source)
    print("Day 2")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

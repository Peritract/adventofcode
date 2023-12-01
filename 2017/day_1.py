def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    

def first_star(data):
    tot = 0
    for i in range(len(data) - 1):
        if data[i] == data[i+1]:
            tot += int(data[i])
    if data[-1] == data[0]:
        tot += int(data[0])
    return tot

def second_star(data):
    print(data)
    tot = 0
    step = len(data) // 2
    for i in range(len(data)):
        if data[i] == data[(i + step) % len(data)]:
            tot += int(data[i])
    return tot


def solution(source):
    data = load_input(source)
    print("Day 1")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

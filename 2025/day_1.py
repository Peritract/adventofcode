def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    
def first_star(data):
    dial = 50
    counter = 0
    for l in data:
        dir, amount = l[0], int(l[1:])
        dial = (dial - amount if dir == "L" else dial + amount) % 100
        if dial == 0:
            counter += 1
    return counter

def second_star(data):
    dial = 50
    counter = 0
    for l in data:
        dir, amount = l[0], int(l[1:])
        if dir == "L":
            for i in range(amount):
                dial -= 1
                dial = dial % 100
                if dial == 0:
                    counter += 1
        else:
            for i in range(amount):
                dial += 1
                dial = dial % 100
                if dial == 0:
                    counter += 1
        print(dial)
    return counter


def solution(source):
    data = load_input(source)
    print("Day 1")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

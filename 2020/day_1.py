def load_input(source):
    with open(source, 'r') as file:
        nums = sorted([int(x) for x in file.readlines()])
    return nums

def first_star(data):
    for i in range(len(data) - 1):
        for j in range(i, len(data)):
            if data[i] + data[j] == 2020:
                    return data[i] * data[j]

def second_star(data):
    for i in range(len(data) - 2):
        for j in range(i, len(data) - 1):
            for k in range(j, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]

def solution(source):
    data = load_input(source)
    print("Day 1")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

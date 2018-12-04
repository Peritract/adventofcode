import re

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

def parse_data(data):
    n_data = [extract_nums(x) for x in data]
    n_data = sorted(n_data, key=lambda line: (line[0],line[1],line[2],line[3],line[4]))
    return n_data

def get_max_index(arr):
    max_i = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_i]:
            max_i = i
    return max_i

def extract_nums(line):
    nums = re.findall(r'\d+', line)
    log = [int(x) for x in nums]
    log.append(line.split(" ")[-1])
    return log

def first_star(data):
    guards = {}
    guard = None
    sleep = None
    for log in data:
        if len(log) == 7:
            if sleep != None:
                for i in range(sleep, 60):
                    guards[guard][i] += 1
            # shift start
            if log[5] not in guards:
                # new guard
                guards[log[5]] = [0 for x in range(60)]
            guard = log[5]
        else:
            if log[-1] == "asleep":
                time = log[4]
                if log[3] == 23:
                    time = 0
                sleep = time
            if log[-1] == "up":
                if sleep != None:
                    for i in range(sleep, log[4]):
                        guards[guard][i] += 1
                sleep = None
    totals = []
    for guard in guards:
        amount = sum(guards[guard])
        index = get_max_index(guards[guard])
        totals.append([guard, amount, index])
    totals = sorted(totals, key=lambda x: x[1], reverse=True)

    return totals[0][0] * totals[0][2]
        

def second_star(data):
    guards = {}
    guard = None
    sleep = None
    for log in data:
        if len(log) == 7:
            if sleep != None:
                for i in range(sleep, 60):
                    guards[guard][i] += 1
            # shift start
            if log[5] not in guards:
                # new guard
                guards[log[5]] = [0 for x in range(60)]
            guard = log[5]
        else:
            if log[-1] == "asleep":
                time = log[4]
                if log[3] == 23:
                    time = 0
                sleep = time
            if log[-1] == "up":
                if sleep != None:
                    for i in range(sleep, log[4]):
                        guards[guard][i] += 1
                sleep = None
    totals = []
    for guard in guards:
        amount = sum(guards[guard])
        index = get_max_index(guards[guard])
        totals.append([guard, guards[guard][index], index])
    totals = sorted(totals, key=lambda x: x[1], reverse=True)

    return totals[0][0] * totals[0][2]


def solution(source):
    data = load_input(source)
    data = parse_data(data)
    print("Day 4")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

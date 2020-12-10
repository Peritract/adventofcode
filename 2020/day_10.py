# I got lost on this one and needed to call out for help; the code is mine but the concept wasn't.

from functools import reduce

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [int(x.strip()) for x in file.readlines()]
    
def first_star(data):
    one = 0
    three = 0
    data.append(0)
    data.append(max(data) + 3)
    data = sorted(data)
    for i in range(len(data) - 1):
        if data[i + 1] - data[i] == 1:
            one += 1
        elif data[i + 1] - data[i] == 3:
            three += 1
    return one * three

def count_runs(data):
    runs = []
    curr_run = 0
    for x in range(len(data) - 1):
        if data[x + 1] - data[x] == 1:
            curr_run += 1
        else:
            runs.append(curr_run)
            curr_run = 0
            
    return runs

def second_star(data):
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    runs = count_runs(data)
    terms = {4: 7, 3: 4, 2 : 2, 1 : 1}
    return reduce(lambda a, b: a * b, [terms[run] for run in runs if run > 0])
    
def solution(source):
    data = load_input(source)
    print("Day 10")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

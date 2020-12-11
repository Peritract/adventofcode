import re
from functools import reduce

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        data = [tuple([int(val) for val in re.findall('-?\d+', line)]) for line in file.readlines()]
        return sorted(data, key=lambda x: x[-1])
    
def manhattan(a, b):
    pairs = list(zip(a, b))
    total = 0
    for pair in pairs:
        s = abs(pair[0] - pair[1])
        total += s
    return total
    
def first_star(data):
    lead = data[-1]
    count = 0
    for bot in data:
        if manhattan(lead[:-1], bot[:-1]) <= lead[-1]:
            count += 1
    return count
    
def second_star(data):
    pass
    
def solution(source):
    data = load_input(source)
    print("Day 23")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

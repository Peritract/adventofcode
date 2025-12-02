import re

def load_input(source):
    with open(source) as f:
        data = [x.strip() for x in f.readlines()]
    if len(data) == 1:
        data = data[0]
    return data
    
def preprocess_data(data):
    return [[int(y) for y in x.split("-")] for x in data.split(",")]

def first_star(data):
    invalid = 0
    for (a, b) in data:
        for i in range(a, b+1):
            if re.match(r"^(\d+)\1$", str(i)):
                invalid += i
    return invalid

def second_star(data):
    invalid = 0
    for (a, b) in data:
        for i in range(a, b+1):
            if re.match(r"^(\d+)\1+$", str(i)):
                invalid += i
    return invalid


def solution(source):
    data = preprocess_data(load_input(source))
    print("Day 2")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("input.txt")

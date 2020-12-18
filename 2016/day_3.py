import re

def load_input(source="input.txt", dim=3):
    with open(source, 'r') as file:
        return [[int(y) for y in re.findall("(\d+)", x)] for x in file.readlines()]

def first_star(data):
    valid = 0
    for tringle in data:
        tringle = sorted(tringle)
        if sum(tringle[:-1]) > tringle[2]:
            valid += 1
    return valid

def second_star(data):
    valid = 0
    for i in range(3):
        trincol = [x[i] for x in data]
        tringles = [sorted(trincol[i:i+3]) for i  in range(0, len(trincol), 3)]
        valid += first_star(tringles)
    return valid
    
def solution(source):
    data = load_input(source)
    print("Day 3")
    print("First star:", str(first_star(data.copy())))
    print("Second star:", str(second_star(data.copy())))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

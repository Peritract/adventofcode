import re

def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line.strip())
    if len(data) == 1:
        data = data[0]
    return data

def first_star(data):
    # Currently a slow brute-force solution
    old = None
    new = data
    while old != new:
        old = new
        for i in "abcdefghijklmnopqrstuvwxyz":
            new = new.replace(i.upper() + i,"")
            new = new.replace(i + i.upper(),"")
    return len(old)        

def second_star(data):
    minimum = None
    n_data = ""
    num = 0
    for i in "abcdefghijklmnopqrstuvwxyz":
        n_data = data.replace(i, "")
        n_data = n_data.replace(i.upper(), "")
        num = first_star(n_data)
        if minimum == None or minimum > num:
            minimum = num
    return minimum


def solution(source):
    data = load_input(source)
    print("Day 5")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

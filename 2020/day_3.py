from functools import reduce

def load_input(source="input.txt"):
    with open(source, 'r') as file:
        return [x.strip() for x in file.readlines()]

def first_star(data, slope=(3,1)):
    loc = [0, 0]
    trees = 0

    while loc[1] < len(data) - 1:
        loc[0] =  (loc[0] + slope[0]) % len(data[0])
        loc[1] += slope[1]
        if data[loc[1]][loc[0]] == "#":
            trees += 1
    return trees

def second_star(data):
    trees = [first_star(data, x) for x in ((1,1), (3,1), (5, 1), (7, 1), (1, 2))]
    return reduce(lambda x, y: x * y, trees, 1)
    
def solution(source):
    data = load_input(source)
    print("Day 2")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")

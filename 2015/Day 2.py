def load_input(source):
    data = []
    with open(source) as file:
        for line in file:
            data.append(line)
    if len(data) == 1:
        data = data[0]
    return data
    
def parse_input(data):
    return [[int(y[0]), int(y[1]), int(y[2])] for y in [x.split("x") for x in data]]
    
def first_star(data):
    total = 0
    for gift in data:
        sides = [gift[0]*gift[1], gift[1]*gift[2], gift[2]*gift[0]]
        total += 2*sides[0] + 2*sides[1] + 2*sides[2] + min(sides)
    return total

def second_star(data):
    total = 0
    for gift in data:
        ribbon = 2 * min([gift[0] + gift[1],gift[1] + gift[2],gift[2]+gift[0]])
        ribbon += gift[0] * gift[1] * gift[2]
        total += ribbon
    return total

def solution(source):
    data = parse_input(load_input(source))
    print("Day N")
    print("First star:", str(first_star(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")

if __name__ == "__main__":
    solution("input.txt")
    
